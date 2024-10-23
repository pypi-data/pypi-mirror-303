from typing import List
import torch
import torch_npu

from ..utils import replace_pattern_with_filters

aten = torch.ops.aten


def fx_pass_fuse_geglu(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]
) -> torch.fx.GraphModule:
    def pattern(x: torch.Tensor):
        chunk = aten.chunk.default(x, 2, -1)
        return aten.mul.Tensor(chunk[0], aten.gelu.default(chunk[1]))

    def replacement(x: torch.Tensor):
        geglu, _ = torch_npu.npu_geglu(x)
        return geglu

    gm = replace_pattern_with_filters(
        gm, pattern, replacement, match_filters=[], name="fuse_geglu"
    )
    return gm
