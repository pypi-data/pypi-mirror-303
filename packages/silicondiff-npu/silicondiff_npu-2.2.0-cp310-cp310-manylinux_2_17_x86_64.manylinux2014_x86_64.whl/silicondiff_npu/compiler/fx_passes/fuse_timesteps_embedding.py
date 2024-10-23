import math
from typing import List

import torch
import torch_npu

from ..utils import replace_pattern_with_filters

aten = torch.ops.aten

import silicondiff_npu


def fx_pass_fuse_timesteps_embedding(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]
) -> torch.fx.GraphModule:
    def pattern_sin_cos(
        timesteps: torch.Tensor,
        arange: torch.Tensor,
        downscale,
        minus_log_max_period,
        extent,
    ):
        mul = aten.mul.Tensor(arange, minus_log_max_period)
        div = aten.div.Tensor(mul, downscale)
        exp = aten.exp.default(div)
        slice_1 = aten.slice.Tensor(timesteps, 0, 0, extent)
        unsqueeze_1 = aten.unsqueeze.default(slice_1, 1)
        to_1 = aten.to.dtype(unsqueeze_1, torch.float32)
        unsqueeze_2 = aten.unsqueeze.default(exp, 0)
        slice_2 = aten.slice.Tensor(unsqueeze_2, 1, 0, extent)
        mul_1 = aten.mul.Tensor(to_1, slice_2)
        sin = aten.sin.default(mul_1)
        cos = aten.cos.default(mul_1)
        cat = aten.cat.default([sin, cos], -1)
        return cat

    def replacement_sin_cos(
        timesteps: torch.Tensor,
        arange: torch.Tensor,
        downscale,
        minus_log_max_period,
        extent,
    ):
        output = silicondiff_npu.ops.timestep_embedding(
            timesteps, arange, downscale, minus_log_max_period, False
        )
        return output

    def pattern_cos_sin(
        timesteps: torch.Tensor,
        arange: torch.Tensor,
        downscale,
        minus_log_max_period,
        extent,
    ):
        mul = aten.mul.Tensor(arange, minus_log_max_period)
        div = aten.div.Tensor(mul, downscale)
        exp = aten.exp.default(div)
        slice_1 = aten.slice.Tensor(timesteps, 0, 0, extent)
        unsqueeze_1 = aten.unsqueeze.default(slice_1, 1)
        to_1 = aten.to.dtype(unsqueeze_1, torch.float32)
        unsqueeze_2 = aten.unsqueeze.default(exp, 0)
        slice_2 = aten.slice.Tensor(unsqueeze_2, 1, 0, extent)
        mul_1 = aten.mul.Tensor(to_1, slice_2)
        sin = aten.sin.default(mul_1)
        cos = aten.cos.default(mul_1)
        cat = aten.cat.default([sin, cos], -1)
        slice_3 = aten.slice.Tensor(cat, 0, 0, extent)
        slice_4 = aten.slice.Tensor(slice_3, 1, downscale, extent)
        slice_6 = aten.slice.Tensor(slice_3, 1, 0, downscale)
        cat_1 = aten.cat.default([slice_4, slice_6], -1)
        return cat_1

    def replacement_cos_sin(
        timesteps: torch.Tensor,
        arange: torch.Tensor,
        downscale,
        minus_log_max_period,
        extent,
    ):
        output = silicondiff_npu.ops.timestep_embedding(
            timesteps, arange, downscale, minus_log_max_period, True
        )
        return output

    for pattern, replacement in [
        (pattern_cos_sin, replacement_cos_sin),
        (pattern_sin_cos, replacement_sin_cos),
    ]:
        gm = replace_pattern_with_filters(
            gm,
            pattern,
            replacement,
            name="fuse_timesteps_embedding",
        )
    return gm
