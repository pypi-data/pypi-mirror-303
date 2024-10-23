from functools import partial, singledispatchmethod
from typing import Optional

import torch

from comfy.controlnet import ControlLora, ControlNet
from comfy.model_patcher import ModelPatcher
from comfy.sd import VAE

from silicondiff_npu import compile

from ..booster_interface import BoosterExecutor
from .silicondiff_controlnet import SiliconDiffControlLora


class SiliconDiffCompileBoosterExecutor(BoosterExecutor):
    # https://pytorch.org/docs/stable/_modules/torch.html#compile
    def __init__(
        self,
        fullgraph=False,
        dynamic=True,
        backend="npu",
        disable=False,
        enable_jit=False,
        enable_memory_format_opt=True,
        options=None,
    ):
        super().__init__()
        if dynamic:
            assert not enable_jit, "must set enable_jit=False when dynamic is True"
        assert backend == "npu", "only npu backend is supported currently"
        options = {} if options is None else options
        self.compile_fn = partial(
            compile,
            fullgraph=fullgraph,
            dynamic=dynamic,
            disable=disable,
            enable_jit=enable_jit,
            enable_memory_format_opt=enable_memory_format_opt,
            **options,
        )
        # self.compile_fn = partial(torch.compile, fullgraph=fullgraph, dynamic=dynamic)
        self.options = options

    @singledispatchmethod
    def execute(self, model, ckpt_name=None, **kwargs):
        raise NotImplementedError(f"Cannot execute {type(model)=}")

    @execute.register(ModelPatcher)
    @torch.inference_mode()
    def _(self, model, ckpt_name: Optional[str] = None, **kwargs):
        diffusion_model = model.model.diffusion_model
        model.model.diffusion_model = self.compile_fn(diffusion_model)
        model.weight_inplace_update = True
        return model

    @execute.register(VAE)
    @torch.inference_mode()
    def _(self, model, ckpt_name: Optional[str] = None, **kwargs):
        print(f"{type(model)} apply compiled config: {self.options}")
        # https://huggingface.co/blog/sd3#performance-optimizations-for-sd3
        model.first_stage_model.decode = self.compile_fn(model.first_stage_model.decode)
        return model

    @execute.register(ControlNet)
    @torch.inference_mode()
    def _(self, model, ckpt_name: Optional[str] = None, **kwargs):
        torch_model = model.control_model
        compiled_model: torch.nn.Module = self.compile_fn(torch_model)
        model.control_model = compiled_model
        return model

    @execute.register(ControlLora)
    @torch.inference_mode()
    def _(self, model, ckpt_name: Optional[str] = None, **kwargs):
        def compile_cnet(model):
            out: torch.nn.Module = self.compile_fn(model)
            return out

        model = SiliconDiffControlLora.from_controllora(model, compile_fn=compile_cnet)
        return model
