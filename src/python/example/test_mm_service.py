import unittest

from z_python_cpp.src.python.service_channel.ipc_service_channel import g_ipc_service_channel

from src.interface.IMmService_pb2 import GeoT, MmType, MmT, MmFilterInputT
from src.interface.IMmService_pb2 import Mm_Stub


class TestStringMethods(unittest.TestCase):
    def test_python_call_cpp_service(self):
        ms = [MmT(geometry=GeoT(height=0, length=0), type=MmType.MmType_NORMAL),
               MmT(geometry=GeoT(height=11.1, length=12.2), type=MmType.MmType_FOOL),
               MmT(geometry=GeoT(height=21.1, length=22.2), type=MmType.MmType_FOOL),
               MmT(geometry=GeoT(height=31.1, length=32.2), type=MmType.MmType_NORMAL)]

        mm_service = Mm_Stub(g_ipc_service_channel)
        target_mm = mm_service.GetMmGeos(None, MmFilterInputT(mms=ms, type=MmType.MmType_FOOL), None)
        self.assertEqual(len(target_mm.ret_geos), 2)
        self.assertEqual(target_mm.ret_geos[0], GeoT(height=11.1, length=12.2))
        self.assertEqual(target_mm.ret_geos[1], GeoT(height=21.1, length=22.2))
        

if __name__ == '__main__':
    unittest.main()