import functools
from typing import List
import torch

from ..utils import replace_pattern_with_filters, match_call_function_input_has_users

aten = torch.ops.aten


def fx_pass_replace_view_with_reshape(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]
) -> torch.fx.GraphModule:
    def pattern_view(x: torch.Tensor, shape: List[int]):
        return aten.view.default(x, shape)

    def pattern__unsafe_view(x: torch.Tensor, shape: List[int]):
        return aten._unsafe_view.default(x, shape)

    def replacement(x: torch.Tensor, shape: List[int]):
        return aten.reshape.default(x, shape)

    gm = replace_pattern_with_filters(
        gm,
        pattern_view,
        replacement,
        match_filters=[
            functools.partial(
                match_call_function_input_has_users, target=aten.view.default, users=1
            )
        ],
        name="replace_view_with_reshape",
    )
    gm = replace_pattern_with_filters(
        gm,
        pattern__unsafe_view,
        replacement,
        match_filters=[
            functools.partial(
                match_call_function_input_has_users,
                target=aten._unsafe_view.default,
                users=1,
            )
        ],
        name="replace__unsafe_view_with_reshape",
    )
    return gm
