#!/usr/bin/python3

from z_python_cpp.src.python.service_channel.ipc_service_channel import g_ipc_service_channel

from src.interface.IMmService_pb2 import GeoT, MmType, MmT, MmFilterInputT
from src.interface.IMmService_pb2 import Mm_Stub

if __name__ == "__main__":
    ms = [MmT(geometry=GeoT(height=0, length=0), type=MmType.MmType_NORMAL),
           MmT(geometry=GeoT(height=11.1, length=12.2), type=MmType.MmType_FOOL),
           MmT(geometry=GeoT(height=21.1, length=22.2), type=MmType.MmType_FOOL),
           MmT(geometry=GeoT(height=31.1, length=32.2), type=MmType.MmType_NORMAL)]

    mm_service = Mm_Stub(g_ipc_service_channel)
    target_mm = mm_service.GetMmGeos(None, MmFilterInputT(mms=ms, type=MmType.MmType_FOOL), None)
    print("Ret: {}".format(target_mm))
