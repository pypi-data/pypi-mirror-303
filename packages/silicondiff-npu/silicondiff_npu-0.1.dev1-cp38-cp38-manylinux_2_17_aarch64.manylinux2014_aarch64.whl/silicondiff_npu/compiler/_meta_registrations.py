import torch
from torch.library import Library, impl

m = Library("silicondiff_npu", "IMPL", "Meta")


# @impl(m, "attention_out")
# def meta_attention_out(
#     input,
#     weight,
#     bias,
# ):
#     shape = input.shape
#     shape[-1] = weight.size(0)
#     return torch.empty(shape, dtype=input.dtype, device=input.device)
