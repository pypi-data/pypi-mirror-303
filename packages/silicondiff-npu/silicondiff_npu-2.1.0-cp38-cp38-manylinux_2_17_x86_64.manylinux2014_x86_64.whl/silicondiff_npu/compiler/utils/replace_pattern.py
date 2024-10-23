import torch


def clean_up_graph_after_modifications(
    gm: torch.fx.GraphModule,
) -> torch.fx.GraphModule:
    """Runs dead-code elimination, linting, and recompilation for graph, in-place"""
    gm.graph.eliminate_dead_code()
    gm.graph.lint()
    gm.recompile()
    return gm


def replace_pattern_with_filters(
    gm,
    pattern,
    replacement,
    *,
    match_filters=None,
    ignore_literals=False,
    name="unknown"
):
    replaced_patterns = torch.fx.subgraph_rewriter.replace_pattern_with_filters(
        gm,
        pattern,
        replacement,
        match_filters=match_filters,
        ignore_literals=ignore_literals,
    )
    if replaced_patterns:
        gm = clean_up_graph_after_modifications(gm)
    return gm


def match_call_function_input_has_users(
    match,
    original_graph: torch.fx.Graph,
    pattern_graph: torch.fx.Graph,
    *,
    target,
    users,
    index=0
) -> bool:
    for node in match.nodes_map.values():
        if node.op == "call_function" and node.target == target:
            if len(node.args) <= index:
                return False
            if not isinstance(node.args[index], torch.fx.Node):
                return False
            return len(node.args[index].users) == users
    return False
