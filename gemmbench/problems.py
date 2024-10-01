# Copyright 2024 The IREE Authors
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from gemm_utils import GemmConfig

def is_compute_bound(M, N, K, bpe):
    """Is this GEMM compute (or memory) bound?"""
    magic_ratio = 64
    flops = 2 * M * N * K
    bytes = bpe * (M * K + K * N + M * N)
    return flops > magic_ratio * bytes


LLAMA = [
    (32000, 1, 8192, "70b", 1),
    (10240, 1, 8192, "70b", 1),
    (8192, 1, 8192, "70b", 1),
    (57344, 1, 8192, "70b", 1),
    (8192, 1, 28672, "70b", 1),
    (10240, 512, 8192, "70b", 1),
    (8192, 512, 8192, "70b", 1),
    (57344, 512, 8192, "70b", 1),
    (8192, 512, 28672, "70b", 1),
    (10240, 1024, 8192, "70b", 1),
    (8192, 1024, 8192, "70b", 1),
    (57344, 1024, 8192, "70b", 1),
    (8192, 1024, 28672, "70b", 1),
    (10240, 2048, 8192, "70b", 1),
    (8192, 2048, 8192, "70b", 1),
    (57344, 2048, 8192, "70b", 1),
    (8192, 2048, 28672, "70b", 1),
    (10240, 3072, 8192, "70b", 1),
    (8192, 3072, 8192, "70b", 1),
    (57344, 3072, 8192, "70b", 1),
    (8192, 3072, 28672, "70b", 1),
    (10240, 4096, 8192, "70b", 1),
    (8192, 4096, 8192, "70b", 1),
    (57344, 4096, 8192, "70b", 1),
    (8192, 4096, 28672, "70b", 1),
    (10240, 5120, 8192, "70b", 1),
    (8192, 5120, 8192, "70b", 1),
    (57344, 5120, 8192, "70b", 1),
    (8192, 5120, 28672, "70b", 1),
    (10240, 6144, 8192, "70b", 1),
    (8192, 6144, 8192, "70b", 1),
    (57344, 6144, 8192, "70b", 1),
    (8192, 6144, 28672, "70b", 1),
    (10240, 7168, 8192, "70b", 1),
    (8192, 7168, 8192, "70b", 1),
    (57344, 7168, 8192, "70b", 1),
    (8192, 7168, 28672, "70b", 1),
    (10240, 8192, 8192, "70b", 1),
    (8192, 8192, 8192, "70b", 1),
    (57344, 8192, 8192, "70b", 1),
    (8192, 8192, 28672, "70b", 1),
    (10240, 9216, 8192, "70b", 1),
    (8192, 9216, 8192, "70b", 1),
    (57344, 9216, 8192, "70b", 1),
    (8192, 9216, 28672, "70b", 1),
    (10240, 10240, 8192, "70b", 1),
    (8192, 10240, 8192, "70b", 1),
    (57344, 10240, 8192, "70b", 1),
    (8192, 10240, 28672, "70b", 1),
    (10240, 11264, 8192, "70b", 1),
    (8192, 11264, 8192, "70b", 1),
    (57344, 11264, 8192, "70b", 1),
    (8192, 11264, 28672, "70b", 1),
    (10240, 12288, 8192, "70b", 1),
    (8192, 12288, 8192, "70b", 1),
    (57344, 12288, 8192, "70b", 1),
    (8192, 12288, 28672, "70b", 1),
    (10240, 13312, 8192, "70b", 1),
    (8192, 13312, 8192, "70b", 1),
    (57344, 13312, 8192, "70b", 1),
    (8192, 13312, 28672, "70b", 1),
    (10240, 14336, 8192, "70b", 1),
    (8192, 14336, 8192, "70b", 1),
    (57344, 14336, 8192, "70b", 1),
    (8192, 14336, 28672, "70b", 1),
    (10240, 15360, 8192, "70b", 1),
    (8192, 15360, 8192, "70b", 1),
    (57344, 15360, 8192, "70b", 1),
    (8192, 15360, 28672, "70b", 1),
    (10240, 16384, 8192, "70b", 1),
    (8192, 16384, 8192, "70b", 1),
    (57344, 16384, 8192, "70b", 1),
    (8192, 16384, 28672, "70b", 1),
    (16000, 1, 8192, "70b", 2),
    (5120, 1, 8192, "70b", 2),
    (8192, 1, 4096, "70b", 2),
    (28672, 1, 8192, "70b", 2),
    (8192, 1, 14336, "70b", 2),
    (5120, 512, 8192, "70b", 2),
    (8192, 512, 4096, "70b", 2),
    (28672, 512, 8192, "70b", 2),
    (8192, 512, 14336, "70b", 2),
    (5120, 1024, 8192, "70b", 2),
    (8192, 1024, 4096, "70b", 2),
    (28672, 1024, 8192, "70b", 2),
    (8192, 1024, 14336, "70b", 2),
    (5120, 2048, 8192, "70b", 2),
    (8192, 2048, 4096, "70b", 2),
    (28672, 2048, 8192, "70b", 2),
    (8192, 2048, 14336, "70b", 2),
    (5120, 3072, 8192, "70b", 2),
    (8192, 3072, 4096, "70b", 2),
    (28672, 3072, 8192, "70b", 2),
    (8192, 3072, 14336, "70b", 2),
    (5120, 4096, 8192, "70b", 2),
    (8192, 4096, 4096, "70b", 2),
    (28672, 4096, 8192, "70b", 2),
    (8192, 4096, 14336, "70b", 2),
    (5120, 5120, 8192, "70b", 2),
    (8192, 5120, 4096, "70b", 2),
    (28672, 5120, 8192, "70b", 2),
    (8192, 5120, 14336, "70b", 2),
    (5120, 6144, 8192, "70b", 2),
    (8192, 6144, 4096, "70b", 2),
    (28672, 6144, 8192, "70b", 2),
    (8192, 6144, 14336, "70b", 2),
    (5120, 7168, 8192, "70b", 2),
    (8192, 7168, 4096, "70b", 2),
    (28672, 7168, 8192, "70b", 2),
    (8192, 7168, 14336, "70b", 2),
    (5120, 8192, 8192, "70b", 2),
    (8192, 8192, 4096, "70b", 2),
    (28672, 8192, 8192, "70b", 2),
    (8192, 8192, 14336, "70b", 2),
    (5120, 9216, 8192, "70b", 2),
    (8192, 9216, 4096, "70b", 2),
    (28672, 9216, 8192, "70b", 2),
    (8192, 9216, 14336, "70b", 2),
    (5120, 10240, 8192, "70b", 2),
    (8192, 10240, 4096, "70b", 2),
    (28672, 10240, 8192, "70b", 2),
    (8192, 10240, 14336, "70b", 2),
    (5120, 11264, 8192, "70b", 2),
    (8192, 11264, 4096, "70b", 2),
    (28672, 11264, 8192, "70b", 2),
    (8192, 11264, 14336, "70b", 2),
    (5120, 12288, 8192, "70b", 2),
    (8192, 12288, 4096, "70b", 2),
    (28672, 12288, 8192, "70b", 2),
    (8192, 12288, 14336, "70b", 2),
    (5120, 13312, 8192, "70b", 2),
    (8192, 13312, 4096, "70b", 2),
    (28672, 13312, 8192, "70b", 2),
    (8192, 13312, 14336, "70b", 2),
    (5120, 14336, 8192, "70b", 2),
    (8192, 14336, 4096, "70b", 2),
    (28672, 14336, 8192, "70b", 2),
    (8192, 14336, 14336, "70b", 2),
    (5120, 15360, 8192, "70b", 2),
    (8192, 15360, 4096, "70b", 2),
    (28672, 15360, 8192, "70b", 2),
    (8192, 15360, 14336, "70b", 2),
    (5120, 16384, 8192, "70b", 2),
    (8192, 16384, 4096, "70b", 2),
    (28672, 16384, 8192, "70b", 2),
    (8192, 16384, 14336, "70b", 2),
    (8000, 1, 8192, "70b", 4),
    (2560, 1, 8192, "70b", 4),
    (8192, 1, 2048, "70b", 4),
    (14336, 1, 8192, "70b", 4),
    (8192, 1, 7168, "70b", 4),
    (2560, 512, 8192, "70b", 4),
    (8192, 512, 2048, "70b", 4),
    (14336, 512, 8192, "70b", 4),
    (8192, 512, 7168, "70b", 4),
    (2560, 1024, 8192, "70b", 4),
    (8192, 1024, 2048, "70b", 4),
    (14336, 1024, 8192, "70b", 4),
    (8192, 1024, 7168, "70b", 4),
    (2560, 2048, 8192, "70b", 4),
    (8192, 2048, 2048, "70b", 4),
    (14336, 2048, 8192, "70b", 4),
    (8192, 2048, 7168, "70b", 4),
    (2560, 3072, 8192, "70b", 4),
    (8192, 3072, 2048, "70b", 4),
    (14336, 3072, 8192, "70b", 4),
    (8192, 3072, 7168, "70b", 4),
    (2560, 4096, 8192, "70b", 4),
    (8192, 4096, 2048, "70b", 4),
    (14336, 4096, 8192, "70b", 4),
    (8192, 4096, 7168, "70b", 4),
    (2560, 5120, 8192, "70b", 4),
    (8192, 5120, 2048, "70b", 4),
    (14336, 5120, 8192, "70b", 4),
    (8192, 5120, 7168, "70b", 4),
    (2560, 6144, 8192, "70b", 4),
    (8192, 6144, 2048, "70b", 4),
    (14336, 6144, 8192, "70b", 4),
    (8192, 6144, 7168, "70b", 4),
    (2560, 7168, 8192, "70b", 4),
    (8192, 7168, 2048, "70b", 4),
    (14336, 7168, 8192, "70b", 4),
    (8192, 7168, 7168, "70b", 4),
    (2560, 8192, 8192, "70b", 4),
    (8192, 8192, 2048, "70b", 4),
    (14336, 8192, 8192, "70b", 4),
    (8192, 8192, 7168, "70b", 4),
    (2560, 9216, 8192, "70b", 4),
    (8192, 9216, 2048, "70b", 4),
    (14336, 9216, 8192, "70b", 4),
    (8192, 9216, 7168, "70b", 4),
    (2560, 10240, 8192, "70b", 4),
    (8192, 10240, 2048, "70b", 4),
    (14336, 10240, 8192, "70b", 4),
    (8192, 10240, 7168, "70b", 4),
    (2560, 11264, 8192, "70b", 4),
    (8192, 11264, 2048, "70b", 4),
    (14336, 11264, 8192, "70b", 4),
    (8192, 11264, 7168, "70b", 4),
    (2560, 12288, 8192, "70b", 4),
    (8192, 12288, 2048, "70b", 4),
    (14336, 12288, 8192, "70b", 4),
    (8192, 12288, 7168, "70b", 4),
    (2560, 13312, 8192, "70b", 4),
    (8192, 13312, 2048, "70b", 4),
    (14336, 13312, 8192, "70b", 4),
    (8192, 13312, 7168, "70b", 4),
    (2560, 14336, 8192, "70b", 4),
    (8192, 14336, 2048, "70b", 4),
    (14336, 14336, 8192, "70b", 4),
    (8192, 14336, 7168, "70b", 4),
    (2560, 15360, 8192, "70b", 4),
    (8192, 15360, 2048, "70b", 4),
    (14336, 15360, 8192, "70b", 4),
    (8192, 15360, 7168, "70b", 4),
    (2560, 16384, 8192, "70b", 4),
    (8192, 16384, 2048, "70b", 4),
    (14336, 16384, 8192, "70b", 4),
    (8192, 16384, 7168, "70b", 4),
    (4000, 1, 8192, "70b", 8),
    (1280, 1, 8192, "70b", 8),
    (8192, 1, 1024, "70b", 8),
    (7168, 1, 8192, "70b", 8),
    (8192, 1, 3584, "70b", 8),
    (1280, 512, 8192, "70b", 8),
    (8192, 512, 1024, "70b", 8),
    (7168, 512, 8192, "70b", 8),
    (8192, 512, 3584, "70b", 8),
    (1280, 1024, 8192, "70b", 8),
    (8192, 1024, 1024, "70b", 8),
    (7168, 1024, 8192, "70b", 8),
    (8192, 1024, 3584, "70b", 8),
    (1280, 2048, 8192, "70b", 8),
    (8192, 2048, 1024, "70b", 8),
    (7168, 2048, 8192, "70b", 8),
    (8192, 2048, 3584, "70b", 8),
    (1280, 3072, 8192, "70b", 8),
    (8192, 3072, 1024, "70b", 8),
    (7168, 3072, 8192, "70b", 8),
    (8192, 3072, 3584, "70b", 8),
    (1280, 4096, 8192, "70b", 8),
    (8192, 4096, 1024, "70b", 8),
    (7168, 4096, 8192, "70b", 8),
    (8192, 4096, 3584, "70b", 8),
    (1280, 5120, 8192, "70b", 8),
    (8192, 5120, 1024, "70b", 8),
    (7168, 5120, 8192, "70b", 8),
    (8192, 5120, 3584, "70b", 8),
    (1280, 6144, 8192, "70b", 8),
    (8192, 6144, 1024, "70b", 8),
    (7168, 6144, 8192, "70b", 8),
    (8192, 6144, 3584, "70b", 8),
    (1280, 7168, 8192, "70b", 8),
    (8192, 7168, 1024, "70b", 8),
    (7168, 7168, 8192, "70b", 8),
    (8192, 7168, 3584, "70b", 8),
    (1280, 8192, 8192, "70b", 8),
    (8192, 8192, 1024, "70b", 8),
    (7168, 8192, 8192, "70b", 8),
    (8192, 8192, 3584, "70b", 8),
    (1280, 9216, 8192, "70b", 8),
    (8192, 9216, 1024, "70b", 8),
    (7168, 9216, 8192, "70b", 8),
    (8192, 9216, 3584, "70b", 8),
    (1280, 10240, 8192, "70b", 8),
    (8192, 10240, 1024, "70b", 8),
    (7168, 10240, 8192, "70b", 8),
    (8192, 10240, 3584, "70b", 8),
    (1280, 11264, 8192, "70b", 8),
    (8192, 11264, 1024, "70b", 8),
    (7168, 11264, 8192, "70b", 8),
    (8192, 11264, 3584, "70b", 8),
    (1280, 12288, 8192, "70b", 8),
    (8192, 12288, 1024, "70b", 8),
    (7168, 12288, 8192, "70b", 8),
    (8192, 12288, 3584, "70b", 8),
    (1280, 13312, 8192, "70b", 8),
    (8192, 13312, 1024, "70b", 8),
    (7168, 13312, 8192, "70b", 8),
    (8192, 13312, 3584, "70b", 8),
    (1280, 14336, 8192, "70b", 8),
    (8192, 14336, 1024, "70b", 8),
    (7168, 14336, 8192, "70b", 8),
    (8192, 14336, 3584, "70b", 8),
    (1280, 15360, 8192, "70b", 8),
    (8192, 15360, 1024, "70b", 8),
    (7168, 15360, 8192, "70b", 8),
    (8192, 15360, 3584, "70b", 8),
    (1280, 16384, 8192, "70b", 8),
    (8192, 16384, 1024, "70b", 8),
    (7168, 16384, 8192, "70b", 8),
    (8192, 16384, 3584, "70b", 8),
    (32000, 1, 5120, "13b", 1),
    (15360, 1, 5120, "13b", 1),
    (5120, 1, 5120, "13b", 1),
    (27648, 1, 5120, "13b", 1),
    (5120, 1, 13824, "13b", 1),
    (15360, 512, 5120, "13b", 1),
    (5120, 512, 5120, "13b", 1),
    (27648, 512, 5120, "13b", 1),
    (5120, 512, 13824, "13b", 1),
    (15360, 1024, 5120, "13b", 1),
    (5120, 1024, 5120, "13b", 1),
    (27648, 1024, 5120, "13b", 1),
    (5120, 1024, 13824, "13b", 1),
    (15360, 2048, 5120, "13b", 1),
    (5120, 2048, 5120, "13b", 1),
    (27648, 2048, 5120, "13b", 1),
    (5120, 2048, 13824, "13b", 1),
    (15360, 3072, 5120, "13b", 1),
    (5120, 3072, 5120, "13b", 1),
    (27648, 3072, 5120, "13b", 1),
    (5120, 3072, 13824, "13b", 1),
    (15360, 4096, 5120, "13b", 1),
    (5120, 4096, 5120, "13b", 1),
    (27648, 4096, 5120, "13b", 1),
    (5120, 4096, 13824, "13b", 1),
    (15360, 5120, 5120, "13b", 1),
    (5120, 5120, 5120, "13b", 1),
    (27648, 5120, 5120, "13b", 1),
    (5120, 5120, 13824, "13b", 1),
    (15360, 6144, 5120, "13b", 1),
    (5120, 6144, 5120, "13b", 1),
    (27648, 6144, 5120, "13b", 1),
    (5120, 6144, 13824, "13b", 1),
    (15360, 7168, 5120, "13b", 1),
    (5120, 7168, 5120, "13b", 1),
    (27648, 7168, 5120, "13b", 1),
    (5120, 7168, 13824, "13b", 1),
    (15360, 8192, 5120, "13b", 1),
    (5120, 8192, 5120, "13b", 1),
    (27648, 8192, 5120, "13b", 1),
    (5120, 8192, 13824, "13b", 1),
    (15360, 9216, 5120, "13b", 1),
    (5120, 9216, 5120, "13b", 1),
    (27648, 9216, 5120, "13b", 1),
    (5120, 9216, 13824, "13b", 1),
    (15360, 10240, 5120, "13b", 1),
    (5120, 10240, 5120, "13b", 1),
    (27648, 10240, 5120, "13b", 1),
    (5120, 10240, 13824, "13b", 1),
    (15360, 11264, 5120, "13b", 1),
    (5120, 11264, 5120, "13b", 1),
    (27648, 11264, 5120, "13b", 1),
    (5120, 11264, 13824, "13b", 1),
    (15360, 12288, 5120, "13b", 1),
    (5120, 12288, 5120, "13b", 1),
    (27648, 12288, 5120, "13b", 1),
    (5120, 12288, 13824, "13b", 1),
    (15360, 13312, 5120, "13b", 1),
    (5120, 13312, 5120, "13b", 1),
    (27648, 13312, 5120, "13b", 1),
    (5120, 13312, 13824, "13b", 1),
    (15360, 14336, 5120, "13b", 1),
    (5120, 14336, 5120, "13b", 1),
    (27648, 14336, 5120, "13b", 1),
    (5120, 14336, 13824, "13b", 1),
    (15360, 15360, 5120, "13b", 1),
    (5120, 15360, 5120, "13b", 1),
    (27648, 15360, 5120, "13b", 1),
    (5120, 15360, 13824, "13b", 1),
    (15360, 16384, 5120, "13b", 1),
    (5120, 16384, 5120, "13b", 1),
    (27648, 16384, 5120, "13b", 1),
    (5120, 16384, 13824, "13b", 1),
    (16000, 1, 5120, "13b", 2),
    (7680, 1, 5120, "13b", 2),
    (5120, 1, 2560, "13b", 2),
    (13824, 1, 5120, "13b", 2),
    (5120, 1, 6912, "13b", 2),
    (7680, 512, 5120, "13b", 2),
    (5120, 512, 2560, "13b", 2),
    (13824, 512, 5120, "13b", 2),
    (5120, 512, 6912, "13b", 2),
    (7680, 1024, 5120, "13b", 2),
    (5120, 1024, 2560, "13b", 2),
    (13824, 1024, 5120, "13b", 2),
    (5120, 1024, 6912, "13b", 2),
    (7680, 2048, 5120, "13b", 2),
    (5120, 2048, 2560, "13b", 2),
    (13824, 2048, 5120, "13b", 2),
    (5120, 2048, 6912, "13b", 2),
    (7680, 3072, 5120, "13b", 2),
    (5120, 3072, 2560, "13b", 2),
    (13824, 3072, 5120, "13b", 2),
    (5120, 3072, 6912, "13b", 2),
    (7680, 4096, 5120, "13b", 2),
    (5120, 4096, 2560, "13b", 2),
    (13824, 4096, 5120, "13b", 2),
    (5120, 4096, 6912, "13b", 2),
    (7680, 5120, 5120, "13b", 2),
    (5120, 5120, 2560, "13b", 2),
    (13824, 5120, 5120, "13b", 2),
    (5120, 5120, 6912, "13b", 2),
    (7680, 6144, 5120, "13b", 2),
    (5120, 6144, 2560, "13b", 2),
    (13824, 6144, 5120, "13b", 2),
    (5120, 6144, 6912, "13b", 2),
    (7680, 7168, 5120, "13b", 2),
    (5120, 7168, 2560, "13b", 2),
    (13824, 7168, 5120, "13b", 2),
    (5120, 7168, 6912, "13b", 2),
    (7680, 8192, 5120, "13b", 2),
    (5120, 8192, 2560, "13b", 2),
    (13824, 8192, 5120, "13b", 2),
    (5120, 8192, 6912, "13b", 2),
    (7680, 9216, 5120, "13b", 2),
    (5120, 9216, 2560, "13b", 2),
    (13824, 9216, 5120, "13b", 2),
    (5120, 9216, 6912, "13b", 2),
    (7680, 10240, 5120, "13b", 2),
    (5120, 10240, 2560, "13b", 2),
    (13824, 10240, 5120, "13b", 2),
    (5120, 10240, 6912, "13b", 2),
    (7680, 11264, 5120, "13b", 2),
    (5120, 11264, 2560, "13b", 2),
    (13824, 11264, 5120, "13b", 2),
    (5120, 11264, 6912, "13b", 2),
    (7680, 12288, 5120, "13b", 2),
    (5120, 12288, 2560, "13b", 2),
    (13824, 12288, 5120, "13b", 2),
    (5120, 12288, 6912, "13b", 2),
    (7680, 13312, 5120, "13b", 2),
    (5120, 13312, 2560, "13b", 2),
    (13824, 13312, 5120, "13b", 2),
    (5120, 13312, 6912, "13b", 2),
    (7680, 14336, 5120, "13b", 2),
    (5120, 14336, 2560, "13b", 2),
    (13824, 14336, 5120, "13b", 2),
    (5120, 14336, 6912, "13b", 2),
    (7680, 15360, 5120, "13b", 2),
    (5120, 15360, 2560, "13b", 2),
    (13824, 15360, 5120, "13b", 2),
    (5120, 15360, 6912, "13b", 2),
    (7680, 16384, 5120, "13b", 2),
    (5120, 16384, 2560, "13b", 2),
    (13824, 16384, 5120, "13b", 2),
    (5120, 16384, 6912, "13b", 2),
    (8000, 1, 5120, "13b", 4),
    (3840, 1, 5120, "13b", 4),
    (5120, 1, 1280, "13b", 4),
    (6912, 1, 5120, "13b", 4),
    (5120, 1, 3456, "13b", 4),
    (3840, 512, 5120, "13b", 4),
    (5120, 512, 1280, "13b", 4),
    (6912, 512, 5120, "13b", 4),
    (5120, 512, 3456, "13b", 4),
    (3840, 1024, 5120, "13b", 4),
    (5120, 1024, 1280, "13b", 4),
    (6912, 1024, 5120, "13b", 4),
    (5120, 1024, 3456, "13b", 4),
    (3840, 2048, 5120, "13b", 4),
    (5120, 2048, 1280, "13b", 4),
    (6912, 2048, 5120, "13b", 4),
    (5120, 2048, 3456, "13b", 4),
    (3840, 3072, 5120, "13b", 4),
    (5120, 3072, 1280, "13b", 4),
    (6912, 3072, 5120, "13b", 4),
    (5120, 3072, 3456, "13b", 4),
    (3840, 4096, 5120, "13b", 4),
    (5120, 4096, 1280, "13b", 4),
    (6912, 4096, 5120, "13b", 4),
    (5120, 4096, 3456, "13b", 4),
    (3840, 5120, 5120, "13b", 4),
    (5120, 5120, 1280, "13b", 4),
    (6912, 5120, 5120, "13b", 4),
    (5120, 5120, 3456, "13b", 4),
    (3840, 6144, 5120, "13b", 4),
    (5120, 6144, 1280, "13b", 4),
    (6912, 6144, 5120, "13b", 4),
    (5120, 6144, 3456, "13b", 4),
    (3840, 7168, 5120, "13b", 4),
    (5120, 7168, 1280, "13b", 4),
    (6912, 7168, 5120, "13b", 4),
    (5120, 7168, 3456, "13b", 4),
    (3840, 8192, 5120, "13b", 4),
    (5120, 8192, 1280, "13b", 4),
    (6912, 8192, 5120, "13b", 4),
    (5120, 8192, 3456, "13b", 4),
    (3840, 9216, 5120, "13b", 4),
    (5120, 9216, 1280, "13b", 4),
    (6912, 9216, 5120, "13b", 4),
    (5120, 9216, 3456, "13b", 4),
    (3840, 10240, 5120, "13b", 4),
    (5120, 10240, 1280, "13b", 4),
    (6912, 10240, 5120, "13b", 4),
    (5120, 10240, 3456, "13b", 4),
    (3840, 11264, 5120, "13b", 4),
    (5120, 11264, 1280, "13b", 4),
    (6912, 11264, 5120, "13b", 4),
    (5120, 11264, 3456, "13b", 4),
    (3840, 12288, 5120, "13b", 4),
    (5120, 12288, 1280, "13b", 4),
    (6912, 12288, 5120, "13b", 4),
    (5120, 12288, 3456, "13b", 4),
    (3840, 13312, 5120, "13b", 4),
    (5120, 13312, 1280, "13b", 4),
    (6912, 13312, 5120, "13b", 4),
    (5120, 13312, 3456, "13b", 4),
    (3840, 14336, 5120, "13b", 4),
    (5120, 14336, 1280, "13b", 4),
    (6912, 14336, 5120, "13b", 4),
    (5120, 14336, 3456, "13b", 4),
    (3840, 15360, 5120, "13b", 4),
    (5120, 15360, 1280, "13b", 4),
    (6912, 15360, 5120, "13b", 4),
    (5120, 15360, 3456, "13b", 4),
    (3840, 16384, 5120, "13b", 4),
    (5120, 16384, 1280, "13b", 4),
    (6912, 16384, 5120, "13b", 4),
    (5120, 16384, 3456, "13b", 4),
    (4000, 1, 5120, "13b", 8),
    (1920, 1, 5120, "13b", 8),
    (5120, 1, 640, "13b", 8),
    (3456, 1, 5120, "13b", 8),
    (5120, 1, 1728, "13b", 8),
    (1920, 512, 5120, "13b", 8),
    (5120, 512, 640, "13b", 8),
    (3456, 512, 5120, "13b", 8),
    (5120, 512, 1728, "13b", 8),
    (1920, 1024, 5120, "13b", 8),
    (5120, 1024, 640, "13b", 8),
    (3456, 1024, 5120, "13b", 8),
    (5120, 1024, 1728, "13b", 8),
    (1920, 2048, 5120, "13b", 8),
    (5120, 2048, 640, "13b", 8),
    (3456, 2048, 5120, "13b", 8),
    (5120, 2048, 1728, "13b", 8),
    (1920, 3072, 5120, "13b", 8),
    (5120, 3072, 640, "13b", 8),
    (3456, 3072, 5120, "13b", 8),
    (5120, 3072, 1728, "13b", 8),
    (1920, 4096, 5120, "13b", 8),
    (5120, 4096, 640, "13b", 8),
    (3456, 4096, 5120, "13b", 8),
    (5120, 4096, 1728, "13b", 8),
    (1920, 5120, 5120, "13b", 8),
    (5120, 5120, 640, "13b", 8),
    (3456, 5120, 5120, "13b", 8),
    (5120, 5120, 1728, "13b", 8),
    (1920, 6144, 5120, "13b", 8),
    (5120, 6144, 640, "13b", 8),
    (3456, 6144, 5120, "13b", 8),
    (5120, 6144, 1728, "13b", 8),
    (1920, 7168, 5120, "13b", 8),
    (5120, 7168, 640, "13b", 8),
    (3456, 7168, 5120, "13b", 8),
    (5120, 7168, 1728, "13b", 8),
    (1920, 8192, 5120, "13b", 8),
    (5120, 8192, 640, "13b", 8),
    (3456, 8192, 5120, "13b", 8),
    (5120, 8192, 1728, "13b", 8),
    (1920, 9216, 5120, "13b", 8),
    (5120, 9216, 640, "13b", 8),
    (3456, 9216, 5120, "13b", 8),
    (5120, 9216, 1728, "13b", 8),
    (1920, 10240, 5120, "13b", 8),
    (5120, 10240, 640, "13b", 8),
    (3456, 10240, 5120, "13b", 8),
    (5120, 10240, 1728, "13b", 8),
    (1920, 11264, 5120, "13b", 8),
    (5120, 11264, 640, "13b", 8),
    (3456, 11264, 5120, "13b", 8),
    (5120, 11264, 1728, "13b", 8),
    (1920, 12288, 5120, "13b", 8),
    (5120, 12288, 640, "13b", 8),
    (3456, 12288, 5120, "13b", 8),
    (5120, 12288, 1728, "13b", 8),
    (1920, 13312, 5120, "13b", 8),
    (5120, 13312, 640, "13b", 8),
    (3456, 13312, 5120, "13b", 8),
    (5120, 13312, 1728, "13b", 8),
    (1920, 14336, 5120, "13b", 8),
    (5120, 14336, 640, "13b", 8),
    (3456, 14336, 5120, "13b", 8),
    (5120, 14336, 1728, "13b", 8),
    (1920, 15360, 5120, "13b", 8),
    (5120, 15360, 640, "13b", 8),
    (3456, 15360, 5120, "13b", 8),
    (5120, 15360, 1728, "13b", 8),
    (1920, 16384, 5120, "13b", 8),
    (5120, 16384, 640, "13b", 8),
    (3456, 16384, 5120, "13b", 8),
    (5120, 16384, 1728, "13b", 8),
]

GPT4 = [
    (16, 16, 1024),
    (16, 16, 8192),
    (16, 16, 65536),
    (16, 2048, 1024),
    (16, 2048, 8192),
    (16, 2048, 65536),
    (16, 8192, 1024),
    (16, 8192, 8192),
    (16, 8192, 65536),
    (2048, 16, 1024),
    (2048, 16, 8192),
    (2048, 16, 65536),
    (2048, 2048, 1024),
    (2048, 2048, 8192),
    (2048, 2048, 65536),
    (2048, 8192, 1024),
    (2048, 8192, 8192),
    (2048, 8192, 65536),
    (8192, 16, 1024),
    (8192, 16, 8192),
    (8192, 16, 65536),
    (8192, 2048, 1024),
    (8192, 2048, 8192),
    (8192, 2048, 65536),
    (8192, 8192, 1024),
    (8192, 8192, 8192),
    (8192, 8192, 65536),
]

UNET = [
    (2048, 10240, 1280),
    (2048, 1280, 1280),
    (2048, 1280, 5120),
    (128, 1280, 2048),
    (8192, 5120, 640),
]

def llama13bmatvec(dtype: str) -> list[GemmConfig]:
    configs = []
    """LLAMA 13b, single batch, FP16."""
    for m, n, k, model, gcount in LLAMA:
        if n == 1 and model == "13b":
            configs.append(GemmConfig(
                m,
                n,
                k,
                "T",
                "N",
                dtype
            ))
    return configs


def llama13bmatvecbf16(dtype: str) -> list[GemmConfig]:
    configs = []
    """LLAMA 13b, single batch, BF16."""
    for m, n, k, model, gcount in LLAMA:
        if n == 1 and model == "13b":
            configs.append(GemmConfig(
                m,
                n,
                k,
                "T",
                "N",
                dtype
            ))
    return configs


def llama70bmatvec(dtype: str) -> list[GemmConfig]:
    """LLAMA 70b, single batch, FP16."""
    configs = []
    for m, n, k, model, gcount in LLAMA:
        if n == 1 and model == "70b":
            configs.append(GemmConfig(
                m,
                n,
                k,
                "T",
                "N",
                dtype
            ))
    return configs


def llama70bmatvecbf16(dtype: str) -> list[GemmConfig]:
    """LLAMA 70b, single batch, BF16."""
    configs = []
    for m, n, k, model, gcount in LLAMA:
        if n == 1 and model == "70b":
            configs.append(GemmConfig(
                m,
                n,
                k,
                "T",
                "N",
                dtype
            ))
    return configs


def llama13bskinny(dtype: str) -> list[GemmConfig]:
    """LLAMA 13b, multiple batches, FP16."""
    configs = []
    for m, n, k, model, gcount in LLAMA:
        if n == 1 and model == "13b":
            for batch in [2, 4, 8, 16, 32]:
                configs.append(GemmConfig(
                    m,
                    batch,
                    k,
                    "T",
                    "N",
                    dtype
                ))
    return configs


def llama13bskinnybf16(dtype: str) -> list[GemmConfig]:
    """LLAMA 13b, multiple batches, BF16."""
    configs = []
    for m, n, k, model, gcount in LLAMA:
        if n == 1 and model == "13b":
            for batch in [2, 4, 8, 16, 32]:
                configs.append(GemmConfig(
                    m,
                    batch,
                    k,
                    "T",
                    "N",
                    dtype
                ))
    return configs


def llama70bskinny(dtype: str) -> list[GemmConfig]:
    """LLAMA 70b, multiple batches, FP16."""
    configs = []
    for m, n, k, model, gcount in LLAMA:
        if n == 1 and model == "70b":
            for batch in [2, 4, 8, 16, 32]:
                configs.append(GemmConfig(
                    m,
                    batch,
                    k,
                    "T",
                    "N",
                    dtype
                ))
    return configs


def llama70bskinnybf16(dtype: str) -> list[GemmConfig]:
    """LLAMA 70b, multiple batches, BF16."""
    configs = []
    for m, n, k, model, gcount in LLAMA:
        if n == 1 and model == "70b":
            for batch in [2, 4, 8, 16, 32]:
                configs.append(GemmConfig(
                    m,
                    batch,
                    k,
                    "T",
                    "N",
                    dtype
                ))
    return configs


def gpt4memory(dtype: str) -> list[GemmConfig]:
    """GPT4 memory bound GEMMs; FP16."""
    configs = []
    for m, n, k in GPT4:
        hgemm = GemmConfig(m, n, k, "N", "N", dtype)
        if not is_compute_bound(m, n, k, 2):
            yield configs.append(hgemm)
    return configs


def gpt4compute(dtype: str) -> list[GemmConfig]:
    """GPT4 compute bound GEMMs; FP16."""
    configs = []
    for m, n, k in GPT4:
        hgemm = GemmConfig(m, n, k, "N", "N", dtype)
        if is_compute_bound(m, n, k, 2):
            configs.append(hgemm)
    return configs


def gpt4clocktest(dtype: str) -> list[GemmConfig]:
    """GPT4 compute bound GEMMs; FP16."""
    configs = []
    macM, macN = 128, 128
    M, N, K = 2048, 2048, 8192
    for mult in range(1, M//macM + 1):
        configs.append(GemmConfig(mult * macM, mult * macN, K, "N", "N", dtype))
    return configs


def test(dtype: str) -> list[GemmConfig]:
    """GPT4 compute bound GEMMs; FP16."""
    #M, N, K = 2048, 2048, 8192
    configs = []
    M, N, K = 128, 128, 8192
    configs.append(GemmConfig(M, N, K, "N", "N", dtype))
    M, N, K = 2048, 2048, 8192
    configs.append(GemmConfig(M, N, K, "N", "N", dtype))
    return configs


def llama70bmemory(dtype: str) -> list[GemmConfig]:
    """LLAMA 70b memory bound GEMMs; NT; BF16."""
    configs = []
    for n in [1280, 3584, 7168]:
        configs.append(GemmConfig(2, n, 8192, "N", "T", dtype))
    return configs


def compute(dtype: str) -> list[GemmConfig]:
    """Compute bound GEMMs."""
    #for dtype in ["fp16", "bf16", "fp8"]:
    configs = []
    for dtype in [dtype]:
        for tA in ["N", "T"]:
            for tB in ["N", "T"]:
                if tA == "N" or tB == "N":
                    configs.append(GemmConfig(4096, 4096, 8192, tA, tB, dtype))
    return configs

def unet(dtype: str) -> list[GemmConfig]:
    configs = []
    for dtype in [dtype]:
        for tA in ["N", "T"]:
            for tB in ["N", "T"]:
                for m, n, k in UNET:
                    if tA == "N" or tB == "N":
                        configs.append(GemmConfig(m, n, k, tA, tB, dtype))
    return configs

def get_gemm_configs() -> list[tuple[str, GemmConfig]]:
    configs: list[tuple[str, GemmConfig]] = []
    llama13bmatvec_configs = llama13bmatvec("f16")
    llama13bmatvec_configs += llama13bmatvecbf16("bf16")
    llama70bmatvec_configs = llama70bmatvec("f16")
    llama70bmatvec_configs += llama70bmatvecbf16("bf16")
    llama13bskinny_configs = llama13bskinny("f16")
    llama13bskinny_configs += llama13bskinnybf16("bf16")
    llama70bskinny_configs = llama70bskinny("f16")
    llama70bskinny_configs += llama70bskinnybf16("bf16")
    gpt4compute_configs = gpt4compute("f16")
    llama70bmemory_configs = llama70bmemory("bf16")
    compute_configs = compute("f16")
    compute_configs += compute("bf16")
    unet_configs = unet("f16")
    unet_configs += unet("bf16")

    configs += [("llama13bmatvec", x) for x in llama13bmatvec_configs]
    configs += [("llama70bmatvec", x) for x in llama70bmatvec_configs]
    configs += [("llama13bskinny", x) for x in llama13bskinny_configs]
    configs += [("llama70bskinny", x) for x in llama70bskinny_configs]
    configs += [("gpt4compute", x) for x in gpt4compute_configs]
    configs += [("llama70bmemory", x) for x in llama70bmemory_configs]
    configs += [("compute", x) for x in compute_configs]
    configs += [("unet", x) for x in unet_configs]
    
    return configs
