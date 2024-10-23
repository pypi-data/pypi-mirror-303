from typing import List, Optional
import torch

from .replace_view_with_reshape import fx_pass_replace_view_with_reshape
from .remove_simple_arith import fx_pass_remove_simple_arith
from .remove_zero_dropout import fx_pass_remove_zero_dropout

from .fuse_attention import fx_pass_fuse_attention
from .fuse_attention_and_qkv_projection import fx_pass_fuse_attention_and_qkv_projection
from .fuse_group_norm import fx_pass_fuse_group_norm
from .fuse_timesteps_embedding import fx_pass_fuse_timesteps_embedding
from .fuse_geglu import fx_pass_fuse_geglu


def apply_fx_passes(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]
) -> torch.fx.GraphModule:
    # import pdb
    # pdb.set_trace()
    # print(gm.graph.print_tabular())

    gm = fx_pass_cse(gm, example_inputs)
    gm = fx_pass_replace_view_with_reshape(gm, example_inputs)
    gm = fx_pass_remove_simple_arith(gm, example_inputs)
    gm = fx_pass_remove_zero_dropout(gm, example_inputs)

    gm = fx_pass_fuse_attention(gm, example_inputs)
    # gm = fx_pass_fuse_attention_and_qkv_projection(gm, example_inputs)
    gm = fx_pass_fuse_group_norm(gm, example_inputs)
    gm = fx_pass_fuse_timesteps_embedding(gm, example_inputs)
    gm = fx_pass_fuse_geglu(gm, example_inputs)

    # print(gm.graph.print_tabular())

    return gm


def fx_pass_cse(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]
) -> torch.fx.GraphModule:
    from torch.fx.passes.dialect.common.cse_pass import CSEPass, get_CSE_banned_ops

    banned_ops = get_CSE_banned_ops()
    P_default = CSEPass(banned_ops=banned_ops)
    gm = P_default(gm).graph_module
    return gm
