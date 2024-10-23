# from packaging import version
# import importlib.metadata
#
# allowed_torch_version = version.parse("2.1.0")
# allowed_torchvision_version = version.parse("0.16.0")
# allowed_torchaudio_version = version.parse("2.1.0")
#
# try:
#     torch_version = version.parse(importlib.metadata.version("torch"))
# except:
#     torch_version = allowed_torch_version
# if torch_version != allowed_torch_version:
#     raise RuntimeError(
#         f"torch version is not supported, please reinstall torch by `pip uninstall torch && pip install torch=={allowed_torch_version}`"
#     )
#
# try:
#     torchvision_version = version.parse(importlib.metadata.version("torchvision"))
# except:
#     torchvision_version = allowed_torchvision_version
# if torchvision_version != allowed_torchvision_version:
#     raise RuntimeError(
#         f"torchvision version is not supported, please reinstall torchvision by `pip uninstall torchvision && pip install torchvision=={allowed_torchvision_version}`"
#     )
#
# try:
#     torchaudio_version = version.parse(importlib.metadata.version("torchaudio"))
# except:
#     torchaudio_version = allowed_torchaudio_version
# if torchaudio_version != allowed_torchaudio_version:
#     raise RuntimeError(
#         f"torchaudio version is not supported, please reinstall torchaudio by `pip uninstall torchaudio && pip install torchaudio=={allowed_torchaudio_version}`"
#     )

import torch
import torch_npu
from torch_npu.contrib import transfer_to_npu
import silicondiff_npu

import comfy
from comfy.cli_args import args
import comfy.model_management
from comfy.model_management import is_device_cpu, is_intel_xpu, ENABLE_PYTORCH_ATTENTION


torch_npu.npu.set_compile_mode(jit_compile=False)


def patch_pytorch_attention_flash_attention():
    if ENABLE_PYTORCH_ATTENTION:
        return True
    return False


def patch_get_free_memory(dev=None, torch_free_too=False):
    # stats = torch.npu.memory_stats(dev)
    # mem_active = stats['active_bytes.all.current']
    # mem_reserved = stats['reserved_bytes.all.current']
    # mem_free_npu, _ = torch.npu.mem_get_info(dev)
    # mem_free_torch = mem_reserved - mem_active
    # mem_free_total = mem_free_npu + mem_free_torch

    mem_free_total = 48 * 1024 * 1024 * 1024  # TODO
    mem_free_torch = mem_free_total

    if torch_free_too:
        return (mem_free_total, mem_free_torch)
    else:
        return mem_free_total


def patch_should_use_fp16(
    device=None, model_params=0, prioritize_performance=True, manual_cast=False
):
    if device is not None:
        if is_device_cpu(device):
            return False
    return True


def patch_should_use_bf16(
    device=None, model_params=0, prioritize_performance=True, manual_cast=False
):
    return False


comfy.model_management.pytorch_attention_flash_attention = (
    patch_pytorch_attention_flash_attention
)
comfy.model_management.get_free_memory = patch_get_free_memory
comfy.model_management.should_use_fp16 = patch_should_use_fp16
comfy.model_management.should_use_bf16 = patch_should_use_bf16
