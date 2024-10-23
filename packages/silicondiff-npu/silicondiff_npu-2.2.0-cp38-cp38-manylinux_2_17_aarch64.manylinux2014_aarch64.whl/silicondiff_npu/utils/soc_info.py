from enum import Enum
import torch_npu


class SocVersion(int, Enum):
    UnsupportedSocVersion = -1
    Ascend910PremiumA = 100
    Ascend910ProA = 101
    Ascend910A = 102
    Ascend910ProB = 103
    Ascend910B = 104
    Ascend310P1 = 200
    Ascend310P2 = 201
    Ascend310P3 = 202
    Ascend310P4 = 203
    Ascend910B1 = 220
    Ascend910B2 = 221
    Ascend910B2C = 222
    Ascend910B3 = 223
    Ascend910B4 = 224
    Ascend310B1 = 240
    Ascend310B2 = 241
    Ascend310B3 = 242
    Ascend310B4 = 243
    Ascend910C1 = 250
    Ascend910C2 = 251
    Ascend910C3 = 252
    Ascend910C4 = 253
    Ascend910D1 = 260


class SocInfo(object):
    def __init__(self):
        torch_npu.npu._lazy_init()
        self.soc_name = torch_npu.npu.get_device_name()
        self.soc_version = SocVersion(torch_npu._C._npu_get_soc_version())
        self.need_nz = self.soc_version in (
            SocVersion.Ascend910PremiumA,
            SocVersion.Ascend910ProA,
            SocVersion.Ascend910A,
            SocVersion.Ascend310P1,
            SocVersion.Ascend310P2,
            SocVersion.Ascend310P3,
            SocVersion.Ascend310P4,
        )


soc_info = None


def get_soc_info():
    global soc_info
    if soc_info is None:
        soc_info = SocInfo()
    return soc_info
