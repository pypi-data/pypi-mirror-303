from typing import List

import torch

from ..utils import replace_pattern_with_filters

aten = torch.ops.aten


def fx_pass_remove_zero_dropout(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]
) -> torch.fx.GraphModule:
    def pattern(
        input_tensor: torch.Tensor,
        is_inplace: bool,
    ):
        ret = aten.dropout.default(input_tensor, 0.0, is_inplace)
        return ret

    def replacement(
        input_tensor: torch.Tensor,
        is_inplace: bool,
    ):
        return input_tensor

    gm = replace_pattern_with_filters(
        gm,
        pattern,
        replacement,
        name="remove_zero_dropout",
    )
    return gm
