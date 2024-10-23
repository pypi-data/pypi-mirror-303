from ..booster_utils import is_optimized_module
from ..hijack_ipadapter_plus.set_model_patch_replace import set_model_patch_replace
from ._config import comfyui_instantid, comfyui_instantid_hijacker

set_model_patch_replace_fn_pt = comfyui_instantid.InstantID._set_model_patch_replace


def cond_func(org_fn, model, *args, **kwargs):
    return is_optimized_module(model)


comfyui_instantid_hijacker.register(
    set_model_patch_replace_fn_pt, set_model_patch_replace, cond_func
)
