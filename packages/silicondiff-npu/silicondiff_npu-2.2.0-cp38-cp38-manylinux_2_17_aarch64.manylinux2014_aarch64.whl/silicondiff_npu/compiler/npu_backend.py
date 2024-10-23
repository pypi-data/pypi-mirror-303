import contextlib
import functools
import unittest
from typing import Any, Dict, List, Optional

import torch
from torch._dynamo.backends.registry import _BACKENDS, register_backend

from torch._dynamo.utils import detect_fake_mode
from torch.fx.experimental.proxy_tensor import make_fx

from .fx_passes import apply_fx_passes
from .utils import patch_decompositions


def _npu_backend(
    gm: torch.fx.GraphModule,
    example_inputs: List[torch.Tensor],
    mode: Optional[str] = None,
    options: Dict[str, Any] = None,
    decompositions: Dict[str, Any] = None,
):
    options = options if options is not None else {}
    fake_mode = detect_fake_mode(example_inputs)
    patch_allow_non_fake_inputs = (
        contextlib.nullcontext()
        if fake_mode is None
        else unittest.mock.patch.object(fake_mode, "allow_non_fake_inputs", True)
    )
    patch_static_shapes = (
        contextlib.nullcontext()
        if (fake_mode is None or not hasattr(fake_mode, "static_shapes"))
        else unittest.mock.patch.object(fake_mode, "static_shapes", True)
    )

    def runnable_gm(*args):
        return torch.fx.Interpreter(gm).run(*args)

    with patch_allow_non_fake_inputs, patch_static_shapes:
        gm = make_fx(
            runnable_gm,
            decomposition_table=decompositions,
            tracing_mode="fake",
            pre_dispatch=True,
            _allow_non_fake_inputs=True,
        )(*example_inputs)

    gm = apply_fx_passes(gm, example_inputs)
    gm.recompile()

    enable_jit = options.get("enable_jit", False)
    if enable_jit:
        return torch.jit.trace(gm, example_inputs)

    return gm


def get_npu_backend(*, custom_decompositions: Dict = {}):
    patch_decompositions()
    decompositions = {}
    decompositions.update(custom_decompositions)
    return functools.partial(_npu_backend, decompositions=decompositions)


def _register_npu_backend(backend):
    if "silicondiff_npu" in _BACKENDS.keys():
        del _BACKENDS["silicondiff_npu"]
    register_backend(backend, "silicondiff_npu")


_DEFAULT_NPU_BACKEND = get_npu_backend()

_register_npu_backend(_DEFAULT_NPU_BACKEND)
