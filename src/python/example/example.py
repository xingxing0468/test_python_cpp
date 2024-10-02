#!/usr/bin/python3

from zed_python_cpp.src.python.service_client.z_service_channel import ZServiceChannel
from zed_python_cpp.src.python.service_probe.service_probe import ZCExtensionServiceProbe

from src.interface.IMmService_pb2 import GeoT, MmType, MmT, MmFilterInputT
from src.interface.IMmService_pb2 import Mm_Stub

import zed_python_cpp.src.cpp.py_binding.zprobe as zprobe

if __name__ == "__main__":
    zprobe.reset_service_path("src/python/example/service_plugins") # runfile path for plugins

    ms = [MmT(geometry=GeoT(height=0, length=0), type=MmType.MmType_NORMAL),
           MmT(geometry=GeoT(height=11.1, length=12.2), type=MmType.MmType_FOOL),
           MmT(geometry=GeoT(height=21.1, length=22.2), type=MmType.MmType_FOOL),
           MmT(geometry=GeoT(height=31.1, length=32.2), type=MmType.MmType_NORMAL)]

    mm_service = Mm_Stub(ZServiceChannel(ZCExtensionServiceProbe()))
    target_mm = mm_service.GetMmGeos(None, MmFilterInputT(mms=ms, type=MmType.MmType_FOOL), None)
    print("Ret: {}".format(target_mm))
