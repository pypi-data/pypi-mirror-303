import torch
from torch._dynamo.eval_frame import OptimizedModule
from .npu_backend import get_npu_backend
from .preprocess_optimize import apply_preprocess_optimizations


def compile(
    module, *, fullgraph=False, dynamic=None, mode=None, disable=False, **options
):
    if disable:
        return module
    module = apply_preprocess_optimizations(module, options)

    class NpuOptimizedModule(OptimizedModule, module.__class__):
        def __init__(self, mod: torch.nn.Module):
            torch.nn.Module.__init__(self)
            self._orig_mod = mod
            self.forward = mod.forward

        def __getattr__(self, name):
            if name == "_orig_mod":
                return self._modules["_orig_mod"]
            return getattr(self._orig_mod, name)

    module = torch.compile(
        module,
        fullgraph=fullgraph,
        dynamic=dynamic,
        mode=mode,
        options=options,
        disable=disable,
        backend=get_npu_backend(),
    )
    return NpuOptimizedModule(module)
