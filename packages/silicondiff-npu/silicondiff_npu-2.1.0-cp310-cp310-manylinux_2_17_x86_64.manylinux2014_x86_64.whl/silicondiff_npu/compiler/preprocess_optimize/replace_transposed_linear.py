import torch
import torch.nn as nn
import torch_npu


class TransposedLinear(nn.Linear):
    def __init__(self, in_features: int, out_features: int, device=None, dtype=None):
        super().__init__(
            in_features, out_features, bias=False, device=device, dtype=dtype
        )
        self.weight.data = self.weight.data.transpose(0, 1).contiguous()

    def forward(self, x, scale=None):
        if scale is not None:
            return torch.matmul(x, self.weight) * scale
        return torch.matmul(x, self.weight)


def recursive_apply(func, module, name=None):
    for subname, submodule in module.named_children():
        func(module, submodule, name, subname)
        recursive_apply(
            func, submodule, f"{name}.{subname}" if name is not None else subname
        )
    return module


def replace_transposed_linear(module):
    def replace(module, submodule, name, subname):
        if isinstance(submodule, nn.Linear) and submodule.bias is None:
            transposed_linear = TransposedLinear(
                submodule.in_features, submodule.out_features
            )
            transposed_linear.weight.data = submodule.weight.data.transpose(
                0, 1
            ).contiguous()
            setattr(module, subname, transposed_linear)

    return recursive_apply(replace, module)
