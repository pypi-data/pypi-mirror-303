import torch
import torch_npu

from .convert_weight_format import (
    convert_linear_weight_format,
    convert_conv_weight_format,
)
from .replace_transposed_linear import replace_transposed_linear


def _get_allow_internal_format_option():
    allow_internal_format = torch_npu._C._npu_getOption("ALLOW_INTERNAL_FORMAT")
    if allow_internal_format == b"disable":
        return False
    return True


def apply_preprocess_optimizations(module, options=None):
    options = {} if options is None else options
    if not options.get("enable_memory_format_opt", True):
        return module
    allow_internal_format = _get_allow_internal_format_option()
    if options.get("allow_internal_format", True):
        torch.npu.config.allow_internal_format = True

    module = replace_transposed_linear(module)
    # module = convert_linear_weight_format(module)  # has no performance improvement
    module = convert_conv_weight_format(module)

    torch.npu.config.allow_internal_format = allow_internal_format
    return module
