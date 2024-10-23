from typing import List
import torch

from ..utils import clean_up_graph_after_modifications

aten = torch.ops.aten


def fx_pass_remove_simple_arith(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]
) -> torch.fx.GraphModule:
    to_erase = []
    for node in gm.graph.nodes:
        if node.op == "call_function":
            if len(node.args) != 2:
                continue
            if node.target in (aten.add.Tensor, aten.sub.Tensor):
                if (
                    isinstance(node.args[0], (int, float))
                    and node.args[0] == 0
                    and len(node.args[1].users) == 1
                ):
                    node.replace_all_uses_with(node.args[1])
                    to_erase.append(node)
                elif (
                    isinstance(node.args[1], (int, float))
                    and node.args[1] == 0
                    and len(node.args[0].users) == 1
                ):
                    node.replace_all_uses_with(node.args[0])
                    to_erase.append(node)
            elif node.target == aten.mul.Tensor:
                if (
                    isinstance(node.args[0], (int, float))
                    and node.args[0] == 1
                    and len(node.args[1].users) == 1
                ):
                    node.replace_all_uses_with(node.args[1])
                    to_erase.append(node)
                elif (
                    isinstance(node.args[1], (int, float))
                    and node.args[1] == 1
                    and len(node.args[0].users) == 1
                ):
                    node.replace_all_uses_with(node.args[0])
                    to_erase.append(node)
            elif node.target == aten.div.Tensor:
                if (
                    isinstance(node.args[1], (int, float))
                    and node.args[1] == 1
                    and len(node.args[0].users) == 1
                ):
                    node.replace_all_uses_with(node.args[0])
                    to_erase.append(node)

    for node in to_erase:
        gm.graph.erase_node(node)

    if to_erase:
        gm = clean_up_graph_after_modifications(gm)
    return gm
