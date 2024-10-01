
module {
    func.func @main(%arg0: tensor<5120x15360xf16>, %arg1: tensor<5120x1xf16>) -> tensor<15360x1xf16> {
        %cst = arith.constant 0.000000e+00 : f16
        %0 = tensor.empty() : tensor<15360x1xf16>
        %1 = linalg.fill ins(%cst : f16) outs(%0 : tensor<15360x1xf16>) -> tensor<15360x1xf16>
        %2 = linalg.matmul_transpose_a ins(%arg0, %arg1 : tensor<5120x15360xf16>, tensor<5120x1xf16>) outs(%1 : tensor<15360x1xf16>) -> tensor<15360x1xf16>
        return %2 : tensor<15360x1xf16>
    }
}
