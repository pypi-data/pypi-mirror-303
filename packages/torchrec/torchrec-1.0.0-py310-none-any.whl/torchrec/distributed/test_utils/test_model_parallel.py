#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

import unittest
from typing import Any, cast, Dict, List, Optional, Tuple, Type

import torch
import torch.nn as nn
from fbgemm_gpu.split_embedding_configs import EmbOptimType
from hypothesis import assume, given, settings, strategies as st, Verbosity
from torchrec.distributed.embedding_types import EmbeddingComputeKernel
from torchrec.distributed.embeddingbag import EmbeddingBagCollectionSharder
from torchrec.distributed.fbgemm_qcomm_codec import CommType, QCommsConfig
from torchrec.distributed.planner import ParameterConstraints
from torchrec.distributed.test_utils.multi_process import MultiProcessTestBase
from torchrec.distributed.test_utils.test_model import TestSparseNN, TestSparseNNBase
from torchrec.distributed.test_utils.test_sharding import (
    create_test_sharder,
    SharderType,
    sharding_single_rank_test,
)
from torchrec.distributed.types import ModuleSharder, ShardingType
from torchrec.modules.embedding_configs import EmbeddingBagConfig, PoolingType
from torchrec.test_utils import seed_and_log, skip_if_asan_class


class ModelParallelTestShared(MultiProcessTestBase):
    @seed_and_log
    def setUp(self, backend: str = "nccl") -> None:
        super().setUp()

        num_features = 4
        num_weighted_features = 2
        shared_features = 2

        self.tables = [
            EmbeddingBagConfig(
                num_embeddings=(i + 1) * 10,
                embedding_dim=(i + 2) * 8,
                name="table_" + str(i),
                feature_names=["feature_" + str(i)],
            )
            for i in range(num_features)
        ]
        shared_features_tables = [
            EmbeddingBagConfig(
                num_embeddings=(i + 1) * 10,
                embedding_dim=(i + 2) * 8,
                name="table_" + str(i + num_features),
                feature_names=["feature_" + str(i)],
            )
            for i in range(shared_features)
        ]
        self.tables += shared_features_tables

        self.mean_tables = [
            EmbeddingBagConfig(
                num_embeddings=(i + 1) * 10,
                embedding_dim=(i + 2) * 8,
                name="table_" + str(i),
                feature_names=["feature_" + str(i)],
                pooling=PoolingType.MEAN,
            )
            for i in range(num_features)
        ]

        shared_features_tables_mean = [
            EmbeddingBagConfig(
                num_embeddings=(i + 1) * 10,
                embedding_dim=(i + 2) * 8,
                name="table_" + str(i + num_features),
                feature_names=["feature_" + str(i)],
                pooling=PoolingType.MEAN,
            )
            for i in range(shared_features)
        ]
        self.mean_tables += shared_features_tables_mean

        self.weighted_tables = [
            EmbeddingBagConfig(
                num_embeddings=(i + 1) * 10,
                embedding_dim=(i + 2) * 4,
                name="weighted_table_" + str(i),
                feature_names=["weighted_feature_" + str(i)],
            )
            for i in range(num_weighted_features)
        ]

        self.shared_features = [f"feature_{i}" for i in range(shared_features)]
        self.embedding_groups = {
            "group_0": [
                (
                    f"{feature}@{table.name}"
                    if feature in self.shared_features
                    else feature
                )
                for table in self.tables
                for feature in table.feature_names
            ]
        }
        self.backend = backend
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        else:
            self.device = torch.device("cpu")

        if self.backend == "nccl" and self.device == torch.device("cpu"):
            self.skipTest("NCCL not supported on CPUs.")

    def _test_sharding(
        self,
        sharders: List[ModuleSharder[nn.Module]],
        backend: str = "gloo",
        world_size: int = 2,
        local_size: Optional[int] = None,
        constraints: Optional[Dict[str, ParameterConstraints]] = None,
        model_class: Type[TestSparseNNBase] = TestSparseNN,
        qcomms_config: Optional[QCommsConfig] = None,
        apply_optimizer_in_backward_config: Optional[
            Dict[str, Tuple[Type[torch.optim.Optimizer], Dict[str, Any]]]
        ] = None,
        variable_batch_size: bool = False,
        variable_batch_per_feature: bool = False,
        has_weighted_tables: bool = True,
        global_constant_batch: bool = False,
        pooling: PoolingType = PoolingType.SUM,
    ) -> None:
        self._run_multi_process_test(
            callable=sharding_single_rank_test,
            world_size=world_size,
            local_size=local_size,
            model_class=model_class,
            tables=self.tables if pooling == PoolingType.SUM else self.mean_tables,
            weighted_tables=self.weighted_tables if has_weighted_tables else None,
            embedding_groups=self.embedding_groups,
            sharders=sharders,
            backend=backend,
            optim=EmbOptimType.EXACT_SGD,
            constraints=constraints,
            qcomms_config=qcomms_config,
            variable_batch_size=variable_batch_size,
            apply_optimizer_in_backward_config=apply_optimizer_in_backward_config,
            variable_batch_per_feature=variable_batch_per_feature,
            global_constant_batch=global_constant_batch,
        )


@skip_if_asan_class
class ModelParallelBase(ModelParallelTestShared):
    def setUp(self, backend: str = "nccl") -> None:
        super().setUp(backend=backend)

    @unittest.skipIf(
        torch.cuda.device_count() <= 1,
        "Not enough GPUs, this test requires at least two GPUs",
    )
    # pyre-fixme[56]
    @given(
        sharder_type=st.sampled_from(
            [
                # SharderType.EMBEDDING_BAG.value,
                SharderType.EMBEDDING_BAG_COLLECTION.value,
            ]
        ),
        kernel_type=st.sampled_from(
            [
                EmbeddingComputeKernel.FUSED.value,
                EmbeddingComputeKernel.FUSED_UVM_CACHING.value,
                EmbeddingComputeKernel.FUSED_UVM.value,
            ],
        ),
        qcomms_config=st.sampled_from(
            [
                None,
                QCommsConfig(
                    forward_precision=CommType.FP16, backward_precision=CommType.BF16
                ),
            ]
        ),
        apply_optimizer_in_backward_config=st.sampled_from(
            [
                None,
                {
                    "embedding_bags": (torch.optim.SGD, {"lr": 0.01}),
                    "embeddings": (torch.optim.SGD, {"lr": 0.2}),
                },
            ]
        ),
        variable_batch_size=st.booleans(),
        pooling=st.sampled_from([PoolingType.SUM, PoolingType.MEAN]),
    )
    @settings(verbosity=Verbosity.verbose, max_examples=6, deadline=None)
    def test_sharding_rw(
        self,
        sharder_type: str,
        kernel_type: str,
        qcomms_config: Optional[QCommsConfig],
        apply_optimizer_in_backward_config: Optional[
            Dict[str, Tuple[Type[torch.optim.Optimizer], Dict[str, Any]]]
        ],
        variable_batch_size: bool,
        pooling: PoolingType,
    ) -> None:
        if self.backend == "gloo":
            self.skipTest(
                "Gloo reduce_scatter_base fallback not supported with async_op=True"
            )

        sharding_type = ShardingType.ROW_WISE.value
        assume(
            sharder_type == SharderType.EMBEDDING_BAG_COLLECTION.value
            or not variable_batch_size
        )

        self._test_sharding(
            sharders=[
                cast(
                    ModuleSharder[nn.Module],
                    create_test_sharder(
                        sharder_type,
                        sharding_type,
                        kernel_type,
                        qcomms_config=qcomms_config,
                        device=self.device,
                    ),
                ),
            ],
            qcomms_config=qcomms_config,
            backend=self.backend,
            apply_optimizer_in_backward_config=apply_optimizer_in_backward_config,
            variable_batch_size=variable_batch_size,
            pooling=pooling,
        )

    # pyre-fixme[56]
    @given(
        sharder_type=st.sampled_from(
            [
                # SharderType.EMBEDDING_BAG.value,
                SharderType.EMBEDDING_BAG_COLLECTION.value,
            ]
        ),
        kernel_type=st.just(EmbeddingComputeKernel.DENSE.value),
        apply_optimizer_in_backward_config=st.just(None),
        # TODO - need to enable optimizer overlapped behavior for data_parallel tables
    )
    @settings(verbosity=Verbosity.verbose, max_examples=1, deadline=None)
    def test_sharding_dp(
        self,
        sharder_type: str,
        kernel_type: str,
        apply_optimizer_in_backward_config: Optional[
            Dict[str, Tuple[Type[torch.optim.Optimizer], Dict[str, Any]]]
        ],
    ) -> None:
        sharding_type = ShardingType.DATA_PARALLEL.value
        self._test_sharding(
            # pyre-ignore[6]
            sharders=[
                create_test_sharder(sharder_type, sharding_type, kernel_type),
            ],
            backend=self.backend,
            apply_optimizer_in_backward_config=apply_optimizer_in_backward_config,
        )

    # pyre-fixme[56]
    @given(
        sharder_type=st.sampled_from(
            [
                # SharderType.EMBEDDING_BAG.value,
                SharderType.EMBEDDING_BAG_COLLECTION.value,
            ]
        ),
        kernel_type=st.sampled_from(
            [
                EmbeddingComputeKernel.FUSED.value,
                EmbeddingComputeKernel.FUSED_UVM_CACHING.value,
                EmbeddingComputeKernel.FUSED_UVM.value,
            ],
        ),
        qcomms_config=st.sampled_from(
            [
                None,
                QCommsConfig(
                    forward_precision=CommType.FP16, backward_precision=CommType.BF16
                ),
            ]
        ),
        apply_optimizer_in_backward_config=st.sampled_from(
            [
                None,
                {
                    "embedding_bags": (torch.optim.SGD, {"lr": 0.01}),
                    "embeddings": (torch.optim.SGD, {"lr": 0.2}),
                },
            ]
        ),
        variable_batch_size=st.booleans(),
    )
    @settings(verbosity=Verbosity.verbose, max_examples=3, deadline=None)
    def test_sharding_cw(
        self,
        sharder_type: str,
        kernel_type: str,
        qcomms_config: Optional[QCommsConfig],
        apply_optimizer_in_backward_config: Optional[
            Dict[str, Tuple[Type[torch.optim.Optimizer], Dict[str, Any]]]
        ],
        variable_batch_size: bool,
    ) -> None:
        if (
            self.device == torch.device("cpu")
            and kernel_type != EmbeddingComputeKernel.FUSED.value
        ):
            self.skipTest("CPU does not support uvm.")

        sharding_type = ShardingType.COLUMN_WISE.value
        assume(
            sharder_type == SharderType.EMBEDDING_BAG_COLLECTION.value
            or not variable_batch_size
        )
        self._test_sharding(
            # pyre-ignore[6]
            sharders=[
                create_test_sharder(
                    sharder_type,
                    sharding_type,
                    kernel_type,
                    qcomms_config=qcomms_config,
                    device=self.device,
                ),
            ],
            backend=self.backend,
            qcomms_config=qcomms_config,
            constraints={
                table.name: ParameterConstraints(min_partition=4)
                for table in self.tables
            },
            apply_optimizer_in_backward_config=apply_optimizer_in_backward_config,
            variable_batch_size=variable_batch_size,
        )

    # pyre-fixme[56]
    @given(
        sharder_type=st.sampled_from(
            [
                # SharderType.EMBEDDING_BAG.value,
                SharderType.EMBEDDING_BAG_COLLECTION.value,
            ]
        ),
        kernel_type=st.sampled_from(
            [
                EmbeddingComputeKernel.FUSED.value,
                EmbeddingComputeKernel.FUSED_UVM_CACHING.value,
                EmbeddingComputeKernel.FUSED_UVM.value,
            ],
        ),
        qcomms_config=st.sampled_from(
            [
                None,
                QCommsConfig(
                    forward_precision=CommType.FP16, backward_precision=CommType.BF16
                ),
            ]
        ),
        apply_optimizer_in_backward_config=st.sampled_from(
            [
                None,
                {
                    "embedding_bags": (torch.optim.SGD, {"lr": 0.01}),
                    "embeddings": (torch.optim.SGD, {"lr": 0.2}),
                },
            ]
        ),
        variable_batch_size=st.booleans(),
    )
    @settings(verbosity=Verbosity.verbose, max_examples=3, deadline=None)
    def test_sharding_twcw(
        self,
        sharder_type: str,
        kernel_type: str,
        qcomms_config: Optional[QCommsConfig],
        apply_optimizer_in_backward_config: Optional[
            Dict[str, Tuple[Type[torch.optim.Optimizer], Dict[str, Any]]]
        ],
        variable_batch_size: bool,
    ) -> None:
        if (
            self.device == torch.device("cpu")
            and kernel_type != EmbeddingComputeKernel.FUSED.value
        ):
            self.skipTest("CPU does not support uvm.")

        sharding_type = ShardingType.TABLE_COLUMN_WISE.value
        assume(
            sharder_type == SharderType.EMBEDDING_BAG_COLLECTION.value
            or not variable_batch_size
        )
        self._test_sharding(
            # pyre-ignore[6]
            sharders=[
                create_test_sharder(
                    sharder_type,
                    sharding_type,
                    kernel_type,
                    qcomms_config=qcomms_config,
                    device=self.device,
                ),
            ],
            backend=self.backend,
            qcomms_config=qcomms_config,
            constraints={
                table.name: ParameterConstraints(min_partition=4)
                for table in self.tables
            },
            apply_optimizer_in_backward_config=apply_optimizer_in_backward_config,
            variable_batch_size=variable_batch_size,
        )

    # pyre-fixme[56]
    @given(
        sharder_type=st.sampled_from(
            [
                # SharderType.EMBEDDING_BAG.value,
                SharderType.EMBEDDING_BAG_COLLECTION.value,
            ]
        ),
        kernel_type=st.sampled_from(
            [
                EmbeddingComputeKernel.FUSED.value,
                EmbeddingComputeKernel.FUSED_UVM_CACHING.value,
                EmbeddingComputeKernel.FUSED_UVM.value,
            ],
        ),
        qcomms_config=st.sampled_from(
            [
                # None,
                QCommsConfig(
                    forward_precision=CommType.FP16,
                    backward_precision=CommType.BF16,
                ),
            ]
        ),
        apply_optimizer_in_backward_config=st.sampled_from(
            [
                None,
                {
                    "embedding_bags": (torch.optim.SGD, {"lr": 0.01}),
                    "embeddings": (torch.optim.SGD, {"lr": 0.2}),
                },
            ]
        ),
        variable_batch_size=st.booleans(),
    )
    @settings(verbosity=Verbosity.verbose, max_examples=3, deadline=None)
    def test_sharding_tw(
        self,
        sharder_type: str,
        kernel_type: str,
        qcomms_config: Optional[QCommsConfig],
        apply_optimizer_in_backward_config: Optional[
            Dict[str, Tuple[Type[torch.optim.Optimizer], Dict[str, Any]]]
        ],
        variable_batch_size: bool,
    ) -> None:
        if (
            self.device == torch.device("cpu")
            and kernel_type != EmbeddingComputeKernel.FUSED.value
        ):
            self.skipTest("CPU does not support uvm.")

        sharding_type = ShardingType.TABLE_WISE.value
        assume(
            sharder_type == SharderType.EMBEDDING_BAG_COLLECTION.value
            or not variable_batch_size
        )
        self._test_sharding(
            # pyre-ignore[6]
            sharders=[
                create_test_sharder(
                    sharder_type,
                    sharding_type,
                    kernel_type,
                    qcomms_config=qcomms_config,
                    device=self.device,
                ),
            ],
            backend=self.backend,
            qcomms_config=qcomms_config,
            apply_optimizer_in_backward_config=apply_optimizer_in_backward_config,
            variable_batch_size=variable_batch_size,
        )

    @unittest.skipIf(
        torch.cuda.device_count() <= 1,
        "Not enough GPUs, this test requires at least two GPUs",
    )
    # pyre-fixme[56]
    @given(
        sharder_type=st.sampled_from(
            [
                # SharderType.EMBEDDING_BAG.value,
                SharderType.EMBEDDING_BAG_COLLECTION.value,
            ]
        ),
        kernel_type=st.sampled_from(
            [
                EmbeddingComputeKernel.FUSED.value,
                EmbeddingComputeKernel.FUSED_UVM_CACHING.value,
                EmbeddingComputeKernel.FUSED_UVM.value,
            ],
        ),
        qcomms_config=st.sampled_from(
            [
                # None,
                QCommsConfig(
                    forward_precision=CommType.FP16,
                    backward_precision=CommType.BF16,
                ),
            ]
        ),
        apply_optimizer_in_backward_config=st.sampled_from(
            [
                None,
                {
                    "embedding_bags": (torch.optim.SGD, {"lr": 0.01}),
                    "embeddings": (torch.optim.SGD, {"lr": 0.2}),
                },
            ]
        ),
        variable_batch_size=st.booleans(),
        pooling=st.sampled_from([PoolingType.SUM, PoolingType.MEAN]),
    )
    @settings(verbosity=Verbosity.verbose, max_examples=6, deadline=None)
    def test_sharding_twrw(
        self,
        sharder_type: str,
        kernel_type: str,
        qcomms_config: Optional[QCommsConfig],
        apply_optimizer_in_backward_config: Optional[
            Dict[str, Tuple[Type[torch.optim.Optimizer], Dict[str, Any]]]
        ],
        variable_batch_size: bool,
        pooling: PoolingType,
    ) -> None:
        if self.backend == "gloo":
            self.skipTest(
                "Gloo reduce_scatter_base fallback not supported with async_op=True"
            )

        sharding_type = ShardingType.TABLE_ROW_WISE.value
        assume(
            sharder_type == SharderType.EMBEDDING_BAG_COLLECTION.value
            or not variable_batch_size
        )
        self._test_sharding(
            # pyre-ignore[6]
            sharders=[
                create_test_sharder(
                    sharder_type,
                    sharding_type,
                    kernel_type,
                    qcomms_config=qcomms_config,
                    device=self.device,
                ),
            ],
            backend=self.backend,
            qcomms_config=qcomms_config,
            apply_optimizer_in_backward_config=apply_optimizer_in_backward_config,
            variable_batch_size=variable_batch_size,
            pooling=pooling,
        )

    @unittest.skipIf(
        torch.cuda.device_count() <= 1,
        "Not enough GPUs, this test requires at least two GPUs",
    )
    # pyre-fixme[56]
    @given(
        sharding_type=st.sampled_from(
            [
                ShardingType.TABLE_WISE.value,
                ShardingType.COLUMN_WISE.value,
                ShardingType.ROW_WISE.value,
                ShardingType.DATA_PARALLEL.value,
            ]
        ),
        global_constant_batch=st.booleans(),
        pooling=st.sampled_from([PoolingType.SUM, PoolingType.MEAN]),
    )
    @settings(verbosity=Verbosity.verbose, max_examples=10, deadline=None)
    def test_sharding_variable_batch(
        self,
        sharding_type: str,
        global_constant_batch: bool,
        pooling: PoolingType,
    ) -> None:
        if self.backend == "gloo":
            # error is from FBGEMM, it says CPU even if we are on GPU.
            self.skipTest(
                "bounds_check_indices on CPU does not support variable length (batch size)"
            )
        kernel = (
            EmbeddingComputeKernel.DENSE.value
            if sharding_type == ShardingType.DATA_PARALLEL.value
            else EmbeddingComputeKernel.FUSED.value
        )
        self._test_sharding(
            # pyre-ignore[6]
            sharders=[
                create_test_sharder(
                    sharder_type=SharderType.EMBEDDING_BAG_COLLECTION.value,
                    sharding_type=sharding_type,
                    kernel_type=kernel,
                    device=self.device,
                ),
            ],
            backend=self.backend,
            constraints={
                table.name: ParameterConstraints(min_partition=4)
                for table in self.tables
            },
            variable_batch_per_feature=True,
            has_weighted_tables=False,
            global_constant_batch=global_constant_batch,
            pooling=pooling,
        )

    @unittest.skipIf(
        torch.cuda.device_count() <= 1,
        "Not enough GPUs, this test requires at least two GPUs",
    )
    # pyre-fixme[56]
    @given(sharding_type=st.just(ShardingType.COLUMN_WISE.value))
    @settings(verbosity=Verbosity.verbose, max_examples=1, deadline=None)
    def test_sharding_multiple_kernels(self, sharding_type: str) -> None:
        if self.backend == "gloo":
            self.skipTest("ProcessGroupGloo does not support reduce_scatter")
        constraints = {
            table.name: ParameterConstraints(
                min_partition=4,
                compute_kernels=(
                    [EmbeddingComputeKernel.FUSED.value]
                    if i % 2 == 0
                    else [EmbeddingComputeKernel.FUSED_UVM_CACHING.value]
                ),
            )
            for i, table in enumerate(self.tables)
        }
        fused_params = {"prefetch_pipeline": True}
        self._test_sharding(
            # pyre-ignore[6]
            sharders=[EmbeddingBagCollectionSharder(fused_params=fused_params)],
            backend=self.backend,
            constraints=constraints,
            variable_batch_per_feature=True,
            has_weighted_tables=False,
        )
