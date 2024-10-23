import torch
import torch_npu
import silicondiff_npu._C

ops = torch.ops.silicondiff_npu

from .compiler import *
from .profiler import *
