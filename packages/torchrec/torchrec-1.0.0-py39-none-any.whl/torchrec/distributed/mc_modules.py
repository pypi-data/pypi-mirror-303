#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

import copy
from collections import defaultdict, OrderedDict
from typing import Any, DefaultDict, Dict, Iterator, List, Optional, Type

import torch
import torch.distributed as dist

from torch import nn
from torch.distributed._shard.sharded_tensor import Shard
from torchrec.distributed.comm import get_local_rank
from torchrec.distributed.embedding import EmbeddingCollectionContext
from torchrec.distributed.embedding_sharding import (
    EmbeddingSharding,
    EmbeddingShardingContext,
    EmbeddingShardingInfo,
    KJTListSplitsAwaitable,
)
from torchrec.distributed.embedding_types import (
    BaseEmbeddingSharder,
    GroupedEmbeddingConfig,
    KJTList,
)
from torchrec.distributed.sharding.rw_sequence_sharding import (
    RwSequenceEmbeddingDist,
    RwSequenceEmbeddingSharding,
)
from torchrec.distributed.sharding.rw_sharding import (
    BaseRwEmbeddingSharding,
    RwSparseFeaturesDist,
)
from torchrec.distributed.sharding.sequence_sharding import SequenceShardingContext
from torchrec.distributed.types import (
    Awaitable,
    LazyAwaitable,
    ParameterSharding,
    QuantizedCommCodecs,
    ShardedModule,
    ShardedTensor,
    ShardingEnv,
    ShardingType,
    ShardMetadata,
)
from torchrec.distributed.utils import append_prefix
from torchrec.modules.mc_modules import ManagedCollisionCollection
from torchrec.modules.utils import construct_jagged_tensors
from torchrec.sparse.jagged_tensor import JaggedTensor, KeyedJaggedTensor


class ManagedCollisionCollectionAwaitable(LazyAwaitable[KeyedJaggedTensor]):
    def __init__(
        self,
        awaitables_per_sharding: List[Awaitable[torch.Tensor]],
        features_per_sharding: List[KeyedJaggedTensor],
        embedding_names_per_sharding: List[List[str]],
        need_indices: bool = False,
        features_to_permute_indices: Optional[Dict[str, List[int]]] = None,
    ) -> None:
        super().__init__()
        self._awaitables_per_sharding = awaitables_per_sharding
        self._features_per_sharding = features_per_sharding
        self._need_indices = need_indices
        self._features_to_permute_indices = features_to_permute_indices
        self._embedding_names_per_sharding = embedding_names_per_sharding

    def _wait_impl(self) -> KeyedJaggedTensor:
        jt_dict: Dict[str, JaggedTensor] = {}
        for w, f, e in zip(
            self._awaitables_per_sharding,
            self._features_per_sharding,
            self._embedding_names_per_sharding,
        ):
            jt_dict.update(
                construct_jagged_tensors(
                    embeddings=w.wait(),
                    features=f,
                    embedding_names=e,
                    need_indices=self._need_indices,
                    features_to_permute_indices=self._features_to_permute_indices,
                )
            )
            # TODO: find better solution
            for jt in jt_dict.values():
                jt._values = jt.values().flatten()
        return KeyedJaggedTensor.from_jt_dict(jt_dict)


class ManagedCollisionCollectionContext(EmbeddingCollectionContext):
    pass


def create_mc_sharding(
    sharding_type: str,
    sharding_infos: List[EmbeddingShardingInfo],
    env: ShardingEnv,
    device: Optional[torch.device] = None,
) -> EmbeddingSharding[
    SequenceShardingContext, KeyedJaggedTensor, torch.Tensor, torch.Tensor
]:
    if sharding_type == ShardingType.ROW_WISE.value:
        return RwSequenceEmbeddingSharding(
            sharding_infos=sharding_infos,
            env=env,
            device=device,
        )
    else:
        raise ValueError(f"Sharding not supported {sharding_type}")


class ShardedManagedCollisionCollection(
    ShardedModule[
        KJTList,
        KJTList,
        KeyedJaggedTensor,
        ManagedCollisionCollectionContext,
    ]
):
    def __init__(
        self,
        module: ManagedCollisionCollection,
        table_name_to_parameter_sharding: Dict[str, ParameterSharding],
        env: ShardingEnv,
        device: torch.device,
        embedding_shardings: List[
            EmbeddingSharding[
                EmbeddingShardingContext,
                KeyedJaggedTensor,
                torch.Tensor,
                torch.Tensor,
            ]
        ],
        qcomm_codecs_registry: Optional[Dict[str, QuantizedCommCodecs]] = None,
    ) -> None:
        super().__init__()
        self._device = device
        self._env = env
        self._table_name_to_parameter_sharding: Dict[str, ParameterSharding] = (
            copy.deepcopy(table_name_to_parameter_sharding)
        )
        # TODO: create a MCSharding type instead of leveraging EmbeddingSharding
        self._embedding_shardings = embedding_shardings

        self._embedding_names_per_sharding: List[List[str]] = []
        for sharding in self._embedding_shardings:
            # TODO: support TWRW sharding
            assert isinstance(
                sharding, BaseRwEmbeddingSharding
            ), "Only ROW_WISE sharding is supported."
            self._embedding_names_per_sharding.append(sharding.embedding_names())

        self._feature_to_table: Dict[str, str] = module._feature_to_table
        self._table_to_features: Dict[str, List[str]] = module._table_to_features
        self._has_uninitialized_input_dists: bool = True
        self._input_dists: List[nn.Module] = []
        self._managed_collision_modules = nn.ModuleDict()
        self._create_managed_collision_modules(module)
        self._output_dists: List[nn.Module] = []
        self._create_output_dists()

        self._initialize_torch_state()

    def _initialize_torch_state(self) -> None:
        self._model_parallel_mc_buffer_name_to_sharded_tensor = OrderedDict()
        shardable_params = set(
            self.sharded_parameter_names(prefix="_managed_collision_modules")
        )

        for fqn, tensor in self.state_dict().items():
            if fqn not in shardable_params:
                continue
            table_name = fqn.split(".")[
                1
            ]  #  "_managed_collision_modules.<table_name>.<param_name>"
            shard_offset, shard_size, global_size = self._mc_module_name_shard_metadata[
                table_name
            ]
            sharded_sizes = list(tensor.shape)
            sharded_sizes[0] = shard_size
            shard_offsets = [0] * len(sharded_sizes)
            shard_offsets[0] = shard_offset
            global_sizes = list(tensor.shape)
            global_sizes[0] = global_size

            self._model_parallel_mc_buffer_name_to_sharded_tensor[fqn] = (
                ShardedTensor._init_from_local_shards(
                    [
                        Shard(
                            tensor=tensor,
                            metadata=ShardMetadata(
                                shard_offsets=shard_offsets,
                                shard_sizes=sharded_sizes,
                                placement=(f"rank:{self._env.rank}/{tensor.device}"),
                            ),
                        )
                    ],
                    torch.Size(global_sizes),
                    process_group=self._env.process_group,
                )
            )

        def _post_state_dict_hook(
            module: ShardedManagedCollisionCollection,
            destination: Dict[str, torch.Tensor],
            prefix: str,
            _local_metadata: Dict[str, Any],
        ) -> None:
            for (
                mc_buffer_name,
                sharded_tensor,
            ) in module._model_parallel_mc_buffer_name_to_sharded_tensor.items():
                destination_key = f"{prefix}{mc_buffer_name}"
                destination[destination_key] = sharded_tensor

        def _load_state_dict_pre_hook(
            module: "ShardedManagedCollisionCollection",
            state_dict: Dict[str, Any],
            prefix: str,
            *args: Any,
        ) -> None:
            for (
                mc_buffer_name,
                _sharded_tensor,
            ) in module._model_parallel_mc_buffer_name_to_sharded_tensor.items():
                key = f"{prefix}{mc_buffer_name}"
                if key in state_dict:
                    if isinstance(state_dict[key], ShardedTensor):
                        local_shards = state_dict[key].local_shards()
                        state_dict[key] = local_shards[0].tensor
                    else:
                        raise RuntimeError(
                            f"Unexpected state_dict key type {type(state_dict[key])} found for {key}"
                        )

        self._register_state_dict_hook(_post_state_dict_hook)
        self._register_load_state_dict_pre_hook(
            _load_state_dict_pre_hook, with_module=True
        )

    def _create_managed_collision_modules(
        self, module: ManagedCollisionCollection
    ) -> None:

        self._mc_module_name_shard_metadata: DefaultDict[str, List[int]] = defaultdict()
        self._feature_to_offset: Dict[str, int] = {}
        self._table_to_offset: Dict[str, int] = {}

        for sharding in self._embedding_shardings:
            assert isinstance(sharding, BaseRwEmbeddingSharding)

            grouped_embedding_configs: List[GroupedEmbeddingConfig] = (
                sharding._grouped_embedding_configs
            )
            for group_config in grouped_embedding_configs:
                for table in group_config.embedding_tables:
                    # pyre-ignore [16]
                    new_min_output_id = table.local_metadata.shard_offsets[0]
                    # pyre-ignore [16]
                    new_range_size = table.local_metadata.shard_sizes[0]
                    output_segments = [
                        x.shard_offsets[0]
                        # pyre-ignore [16]
                        for x in table.global_metadata.shards_metadata
                    ] + [table.num_embeddings]
                    mc_module = module._managed_collision_modules[table.name]

                    self._managed_collision_modules[table.name] = (
                        mc_module.rebuild_with_output_id_range(
                            output_id_range=(
                                new_min_output_id,
                                new_min_output_id + new_range_size,
                            ),
                            output_segments=output_segments,
                            device=self._device,
                        )
                    )
                    zch_size = self._managed_collision_modules[table.name]._zch_size

                    zch_size_by_rank = [
                        torch.zeros(1, dtype=torch.int64, device=self._device)
                        for _ in range(self._env.world_size)
                    ]
                    if self._env.world_size > 1:
                        dist.all_gather(
                            zch_size_by_rank,
                            torch.tensor(
                                [zch_size], dtype=torch.int64, device=self._device
                            ),
                            group=self._env.process_group,
                        )
                    else:
                        zch_size_by_rank[0] = torch.tensor(
                            [zch_size], dtype=torch.int64, device=self._device
                        )

                    # Calculate the sum of all ZCH sizes from rank 0 to list
                    # index. The last item is the sum of all elements in zch_size_by_rank
                    zch_size_cumsum = torch.cumsum(
                        torch.cat(zch_size_by_rank), dim=0
                    ).tolist()

                    zch_size_sum_before_this_rank = (
                        zch_size_cumsum[self._env.rank] - zch_size
                    )

                    self._mc_module_name_shard_metadata[table.name] = (
                        zch_size_sum_before_this_rank,
                        zch_size,
                        zch_size_cumsum[-1],
                    )
                    for feature in table.feature_names:
                        self._feature_to_offset[feature] = new_min_output_id
                    self._table_to_offset[table.name] = new_min_output_id

    def _create_input_dists(
        self,
        input_feature_names: List[str],
    ) -> None:
        feature_names: List[str] = []
        self._feature_splits: List[int] = []
        for sharding in self._embedding_shardings:
            assert isinstance(sharding, BaseRwEmbeddingSharding)
            feature_hash_sizes: List[int] = [
                self._managed_collision_modules[self._feature_to_table[f]].input_size()
                for f in sharding.feature_names()
            ]

            input_dist = RwSparseFeaturesDist(
                # pyre-ignore [6]
                pg=sharding._pg,
                num_features=sharding._get_num_features(),
                feature_hash_sizes=feature_hash_sizes,
                device=sharding._device,
                is_sequence=True,
                has_feature_processor=sharding._has_feature_processor,
                need_pos=False,
                keep_original_indices=True,
            )
            self._input_dists.append(input_dist)
            feature_names.extend(sharding.feature_names())
            self._feature_splits.append(len(sharding.feature_names()))

        self._features_order: List[int] = []
        for f in feature_names:
            self._features_order.append(input_feature_names.index(f))
        self._features_order = (
            []
            if self._features_order == list(range(len(self._features_order)))
            else self._features_order
        )
        self.register_buffer(
            "_features_order_tensor",
            torch.tensor(self._features_order, device=self._device, dtype=torch.int32),
            persistent=False,
        )

    def _create_output_dists(
        self,
    ) -> None:
        for sharding in self._embedding_shardings:
            assert isinstance(sharding, BaseRwEmbeddingSharding)
            self._output_dists.append(
                RwSequenceEmbeddingDist(
                    # pyre-ignore [6]
                    sharding._pg,
                    sharding._get_num_features(),
                    sharding._device,
                )
            )

    # pyre-ignore [14]
    def input_dist(
        self,
        ctx: ManagedCollisionCollectionContext,
        features: KeyedJaggedTensor,
    ) -> Awaitable[Awaitable[KJTList]]:
        if self._has_uninitialized_input_dists:
            self._create_input_dists(input_feature_names=features.keys())
            self._has_uninitialized_input_dists = False

        with torch.no_grad():
            features_dict = features.to_dict()
            output: Dict[str, JaggedTensor] = features_dict.copy()
            for table, mc_module in self._managed_collision_modules.items():
                feature_list: List[str] = self._table_to_features[table]
                mc_input: Dict[str, JaggedTensor] = {}
                for feature in feature_list:
                    mc_input[feature] = features_dict[feature]
                mc_input = mc_module.preprocess(mc_input)
                output.update(mc_input)

            # NOTE shared features not currently supported
            features = KeyedJaggedTensor.from_jt_dict(output)

            if self._features_order:
                features = features.permute(
                    self._features_order,
                    self._features_order_tensor,
                )
            features_by_sharding = features.split(
                self._feature_splits,
            )
            awaitables = []
            for input_dist, features in zip(self._input_dists, features_by_sharding):
                awaitables.append(input_dist(features))
                ctx.sharding_contexts.append(
                    SequenceShardingContext(
                        features_before_input_dist=features,
                        unbucketize_permute_tensor=(
                            input_dist.unbucketize_permute_tensor
                            if isinstance(input_dist, RwSparseFeaturesDist)
                            else None
                        ),
                    )
                )

        return KJTListSplitsAwaitable(awaitables, ctx)

    def _kjt_list_to_tensor_list(
        self,
        kjt_list: KJTList,
        feature_to_offset: Dict[str, int],
    ) -> List[torch.Tensor]:
        remapped_ids_ret: List[torch.Tensor] = []
        # TODO: find a better solution
        for kjt in kjt_list:
            jt_dict = kjt.to_dict()
            for feature, jt in jt_dict.items():
                offset = feature_to_offset[feature]
                jt._values = jt.values().add(offset)
            new_kjt = KeyedJaggedTensor.from_jt_dict(jt_dict)
            remapped_ids_ret.append(new_kjt.values().view(-1, 1))
        return remapped_ids_ret

    def global_to_local_index(
        self,
        feature_dict: Dict[str, JaggedTensor],
    ) -> Dict[str, JaggedTensor]:
        for feature, jt in feature_dict.items():
            jt._values = jt.values() - self._feature_to_offset[feature]
        return feature_dict

    def compute(
        self,
        ctx: ManagedCollisionCollectionContext,
        dist_input: KJTList,
    ) -> KJTList:
        remapped_kjts: List[KeyedJaggedTensor] = []

        for features, sharding_ctx in zip(
            dist_input,
            ctx.sharding_contexts,
        ):
            sharding_ctx.lengths_after_input_dist = features.lengths().view(
                -1, features.stride()
            )
            features_dict = features.to_dict()
            output: Dict[str, JaggedTensor] = features_dict.copy()
            for table, mc_module in self._managed_collision_modules.items():
                feature_list: List[str] = self._table_to_features[table]
                mc_input: Dict[str, JaggedTensor] = {}
                for feature in feature_list:
                    mc_input[feature] = features_dict[feature]
                mc_input = mc_module.profile(mc_input)
                mc_input = mc_module.remap(mc_input)
                mc_input = self.global_to_local_index(mc_input)
                output.update(mc_input)

            remapped_kjts.append(KeyedJaggedTensor.from_jt_dict(output))
        return KJTList(remapped_kjts)

    def evict(self) -> Dict[str, Optional[torch.Tensor]]:
        evictions: Dict[str, Optional[torch.Tensor]] = {}
        for (
            table,
            managed_collision_module,
        ) in self._managed_collision_modules.items():
            global_indices_to_evict = managed_collision_module.evict()
            local_indices_to_evict = None
            if global_indices_to_evict is not None:
                local_indices_to_evict = (
                    global_indices_to_evict - self._table_to_offset[table]
                )
            evictions[table] = local_indices_to_evict
        return evictions

    def open_slots(self) -> Dict[str, torch.Tensor]:
        open_slots: Dict[str, torch.Tensor] = {}
        for (
            table,
            managed_collision_module,
        ) in self._managed_collision_modules.items():
            open_slots[table] = managed_collision_module.open_slots()
        return open_slots

    def output_dist(
        self,
        ctx: ManagedCollisionCollectionContext,
        output: KJTList,
    ) -> LazyAwaitable[KeyedJaggedTensor]:

        global_remapped = self._kjt_list_to_tensor_list(output, self._feature_to_offset)
        awaitables_per_sharding: List[Awaitable[torch.Tensor]] = []
        features_before_all2all_per_sharding: List[KeyedJaggedTensor] = []
        for odist, remapped_ids, sharding_ctx in zip(
            self._output_dists,
            global_remapped,
            ctx.sharding_contexts,
        ):
            awaitables_per_sharding.append(odist(remapped_ids, sharding_ctx))
            features_before_all2all_per_sharding.append(
                # pyre-fixme[6]: For 1st argument expected `KeyedJaggedTensor` but
                #  got `Optional[KeyedJaggedTensor]`.
                sharding_ctx.features_before_input_dist
            )
        return ManagedCollisionCollectionAwaitable(
            awaitables_per_sharding=awaitables_per_sharding,
            features_per_sharding=features_before_all2all_per_sharding,
            embedding_names_per_sharding=self._embedding_names_per_sharding,
            need_indices=False,
            features_to_permute_indices=None,
        )

    def create_context(self) -> ManagedCollisionCollectionContext:
        return ManagedCollisionCollectionContext(sharding_contexts=[])

    def sharded_parameter_names(self, prefix: str = "") -> Iterator[str]:
        for name, module in self._managed_collision_modules.items():
            module_prefix = append_prefix(prefix, name)
            for name, _ in module.named_buffers():
                if name in ["_output_segments_tensor", "_current_iter_tensor"]:
                    continue
                if name in module._non_persistent_buffers_set:
                    continue
                yield append_prefix(module_prefix, name)
            for name, _ in module.named_parameters():
                yield append_prefix(module_prefix, name)


class ManagedCollisionCollectionSharder(
    BaseEmbeddingSharder[ManagedCollisionCollection]
):
    def __init__(
        self,
        qcomm_codecs_registry: Optional[Dict[str, QuantizedCommCodecs]] = None,
    ) -> None:
        super().__init__(qcomm_codecs_registry=qcomm_codecs_registry)

    def shard(
        self,
        module: ManagedCollisionCollection,
        params: Dict[str, ParameterSharding],
        env: ShardingEnv,
        embedding_shardings: List[
            EmbeddingSharding[
                EmbeddingShardingContext,
                KeyedJaggedTensor,
                torch.Tensor,
                torch.Tensor,
            ]
        ],
        device: Optional[torch.device] = None,
    ) -> ShardedManagedCollisionCollection:

        if device is None:
            device = torch.device("cpu")

        return ShardedManagedCollisionCollection(
            module,
            params,
            env=env,
            device=device,
            embedding_shardings=embedding_shardings,
        )

    def shardable_parameters(
        self, module: ManagedCollisionCollection
    ) -> Dict[str, torch.nn.Parameter]:
        # TODO: standalone sharding
        raise NotImplementedError()

    @property
    def module_type(self) -> Type[ManagedCollisionCollection]:
        return ManagedCollisionCollection

    def sharding_types(self, compute_device_type: str) -> List[str]:
        types = [
            ShardingType.ROW_WISE.value,
        ]
        return types
