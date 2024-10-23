import torch
import torch.nn as nn
import torch_npu

from .replace_transposed_linear import TransposedLinear


def convert_linear_weight_format(module):
    for name, m in module.named_modules():
        if (
            (isinstance(m, nn.Linear) or isinstance(m, TransposedLinear))
            and not torch.npu.get_mm_bmm_format_nd()
            and m.weight.dtype == torch.float16
        ):
            m.weight.data = torch_npu.npu_format_cast(
                m.weight.data, 29
            )  # ACL_FORMAT_FRACTAL_NZ
    return module


def convert_conv_weight_format(module):
    for name, m in module.named_modules():
        if isinstance(m, nn.Conv2d):
            if m.groups > 1 or m.weight.dtype != torch.float16:
                continue
            m.weight.data = torch_npu.npu_format_cast(
                m.weight.data, 4
            )  # ACL_FORMAT_FRACTAL_Z
    return module
