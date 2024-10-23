from typing import Callable, cast, Iterable, List, Optional, Tuple, Union

import torch
import torch._prims as prims
import torch._prims_common as utils
from torch import sym_float, sym_int, Tensor

from torch._decomp.decompositions import (
    upsample_compute_output_size,
    get_scale_value,
    _compute_upsample_nearest_indices,
)

aten = torch._ops.ops.aten


def upsample_nearest1d_vec(input, output_size, scale_factors):
    osize = upsample_compute_output_size(input.size(), output_size, scale_factors)
    scale = get_scale_value(scale_factors, 0)

    return upsample_nearest1d(input, osize, scale)


def upsample_nearest2d_vec(input, output_size, scale_factors):
    osize = upsample_compute_output_size(input.size(), output_size, scale_factors)
    scale_h = get_scale_value(scale_factors, 0)
    scale_w = get_scale_value(scale_factors, 1)

    return upsample_nearest2d(input, osize, scale_h, scale_w)


def upsample_nearest3d_vec(input, output_size, scale_factors):
    osize = upsample_compute_output_size(input.size(), output_size, scale_factors)
    scale_d = get_scale_value(scale_factors, 0)
    scale_h = get_scale_value(scale_factors, 1)
    scale_w = get_scale_value(scale_factors, 2)

    return upsample_nearest3d(input, osize, scale_d, scale_h, scale_w)


def upsample_nearest1d(
    input: Tensor,
    output_size: List[int],
    scales: Optional[float] = None,
) -> Tensor:
    (l_indices,) = _compute_upsample_nearest_indices(input, output_size, (scales,))
    return aten._unsafe_index(input, (None, None, l_indices))


def upsample_nearest2d(
    input: Tensor,
    output_size: List[int],
    scales_h: Optional[float] = None,
    scales_w: Optional[float] = None,
) -> Tensor:
    h_indices, w_indices = _compute_upsample_nearest_indices(
        input, output_size, (scales_h, scales_w)
    )
    result = aten._unsafe_index(input, (None, None, h_indices, w_indices))

    # convert output to correct memory format, if necessary
    memory_format = utils.suggest_memory_format(input)

    # following "heuristic: only use channels_last path when it's faster than the contiguous path"
    _, n_channels, _, _ = input.shape
    if input.device.type == "cuda" and n_channels < 4:
        memory_format = torch.contiguous_format

    result = result.contiguous(memory_format=memory_format)

    return result


def upsample_nearest3d(
    input: Tensor,
    output_size: List[int],
    scales_d: Optional[float] = None,
    scales_h: Optional[float] = None,
    scales_w: Optional[float] = None,
) -> Tensor:
    d_indices, h_indices, w_indices = _compute_upsample_nearest_indices(
        input, output_size, (scales_d, scales_h, scales_w)
    )
    result = aten._unsafe_index(input, (None, None, d_indices, h_indices, w_indices))

    return result


def patch_decompositions():
    from torch._decomp import decomposition_table, register_decomposition
    from torch._C import DispatchKey

    """
    torch_npu will remove some implicitly decompose implementations of some aten ops,
    but this may cause errors during torch.compile with dynamic mode, so we need patch
    the implicitly decompose implementations.
    """
    aten_ops = {
        "aten.upsample_nearest1d.vec": upsample_nearest1d_vec,
        # "aten.upsample_nearest1d.default": upsample_nearest1d,
        "aten.upsample_nearest2d.vec": upsample_nearest2d_vec,
        # "aten.upsample_nearest2d.default": upsample_nearest2d,
        "aten.upsample_nearest3d.vec": upsample_nearest3d_vec,
        # "aten.upsample_nearest3d.default": upsample_nearest3d,
    }
    for op_override in decomposition_table.keys():
        if str(op_override) in aten_ops:
            if DispatchKey.CompositeImplicitAutograd not in op_override.py_kernels:
                fn = aten_ops[str(op_override)]
                register_decomposition(op_override, fn)
                op_override.py_impl(DispatchKey.CompositeImplicitAutograd)(fn)
