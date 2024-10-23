from comfy.model_base import BaseModel
from comfy.model_patcher import ModelPatcher
from torch._dynamo.eval_frame import OptimizedModule


def clear_deployable_module_cache_and_unbind(*args, **kwargs):
    raise RuntimeError(f"TODO")


def is_optimized_module(module):
    if isinstance(module, ModelPatcher):
        if hasattr(module.model, "diffusion_model"):
            diff_model = module.model.diffusion_model
            return isinstance(diff_model, OptimizedModule)
    if isinstance(module, BaseModel):
        if hasattr(module, "diffusion_model"):
            return isinstance(module.diffusion_model, OptimizedModule)
    return False
