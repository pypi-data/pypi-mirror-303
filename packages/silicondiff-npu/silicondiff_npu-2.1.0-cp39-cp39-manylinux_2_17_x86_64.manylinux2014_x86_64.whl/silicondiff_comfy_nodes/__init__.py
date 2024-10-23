"""SiliconDiff ComfyUI Speedup Module"""

from ._nodes import (
    ControlnetSpeedup,
    ModelSpeedup,
    SiliconDiffApplyModelBooster,
    SiliconDiffCheckpointLoaderSimple,
    SiliconDiffControlNetLoader,
    VaeSpeedup,
)

NODE_CLASS_MAPPINGS = {
    "ModelSpeedup": ModelSpeedup,
    "VaeSpeedup": VaeSpeedup,
    "ControlnetSpeedup": ControlnetSpeedup,
    "SiliconDiffModelBooster": SiliconDiffApplyModelBooster,
    "SiliconDiffCheckpointLoaderSimple": SiliconDiffCheckpointLoaderSimple,
    "SiliconDiffControlNetLoader": SiliconDiffControlNetLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ModelSpeedup": "Model Speedup",
    "VaeSpeedup": "VAE Speedup",
    "SiliconDiffModelBooster": "Apply Model Booster - SiliconDiff",
    "ControlnetSpeedup": "ControlNet Speedup",
    "SiliconDiffCheckpointLoaderSimple": "Load Checkpoint - SiliconDiff",
}


def update_node_mappings(node):
    NODE_CLASS_MAPPINGS.update(node.NODE_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(node.NODE_DISPLAY_NAME_MAPPINGS)


def lazy_load_extra_nodes():

    from .extras_nodes import nodes_silicondiff_compile_booster
    from .extras_nodes import nodes_prompt_styler

    update_node_mappings(nodes_silicondiff_compile_booster)
    update_node_mappings(nodes_prompt_styler)


# Lazy load all extra nodes when needed
lazy_load_extra_nodes()
