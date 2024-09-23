#!/usr/bin/python3

from src.python.service_client.z_service_channel import ZServiceChannel
from src.python.service_probe.service_probe import ZCExtensionServiceProbe

from src.interface.IMmService_pb2 import GeoT, MmType, MmT, MmFilterInputT
from src.interface.IMmService_pb2 import Mm_Stub

import src.cpp.py_binding.zprobe as zprobe

if __name__ == "__main__":
    zprobe.reset_service_path("src/python/example/service_plugins") # runfile path for plugins

    ms = [MmT(position=GeoT(height=0, length=0), type=MmType.NORMAL),
           MmT(position=GeoT(height=11.1, length=12.2), type=MmType.MMTYPE_FOOL),
           MmT(position=GeoT(height=21.1, length=22.2), type=MmType.MMTYPE_FOOL),
           MmT(position=GeoT(height=31.1, length=32.2), type=MmType.MMTYPE_NORMAL)]

    mm_service = Mm_Stub(ZServiceChannel(ZCExtensionServiceProbe()))
    target_mm = mm_service.GetMmGeos(None, MmFilterInputT(mms=ms, type=MmType.FOOL), None)
    print("Ret: {}".format(target_mm))
