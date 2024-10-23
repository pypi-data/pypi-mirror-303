import ctypes

import cv2
import numpy as np
from mmumu import MuMuApi

from msc import ScreenCap


class MuMuScreenCap(ScreenCap):
    MUMU_INSTALL_PATH = r"C:\Program Files\Netease\MuMu Player 12"
    MUMU_API_DLL_PATH = r"\shell\sdk\external_renderer_ipc.dll"

    def __init__(
            self,
            instance_index: int,
            emulator_install_path: str = None,
            dll_path: str = None,
            display_id: int = 0
    ):
        """
        __init__ MumuApi 截图

        基于/shell/sdk/external_renderer_ipc.dll实现截图mumu模拟器

        Args:
            instance_index (int): 模拟器实例的编号
            emulator_install_path (str): 模拟器安装路径，一般会根据模拟器注册表路径获取. Defaults to None.
            dll_path (str, optional): dll文件存放路径，一般会根据模拟器路径获取. Defaults to None.
            display_id (int, optional): 显示窗口id，一般无需填写. Defaults to 0.
        """
        self.display_id = display_id
        self.instance_index = instance_index
        self.emulator_install_path = emulator_install_path
        self.dllPath = emulator_install_path + \
                       self.MUMU_API_DLL_PATH if dll_path is None else dll_path

        self.width: int
        self.height: int
        self.buffer_size: int

        self.nemu = MuMuApi(self.dllPath)
        # 连接模拟器
        self.handle = self.nemu.connect(
            self.emulator_install_path, self.instance_index)
        self.__get_display_info()

    def __get_display_info(self):
        width = ctypes.c_int(0)
        height = ctypes.c_int(0)
        result = self.nemu.capture_display(
            self.handle,
            self.display_id,
            0,
            ctypes.byref(width),
            ctypes.byref(height),
            None,
        )
        if result != 0:
            print("Failed to get the display size.")
            return None
        self.width, self.height = width.value, height.value
        # 根据宽度和高度计算缓冲区大小
        self.buffer_size = self.width * self.height * 4
        # 创建一个足够大的缓冲区来存储像素数据
        self.pixels = (ctypes.c_ubyte * self.buffer_size)()

    def __buffer2opencv(self) -> cv2.Mat:
        # Directly use the pixel buffer and reshape only once
        pixel_array = np.frombuffer(self.pixels, dtype=np.uint8).reshape((self.height, self.width, 4))
        return cv2.cvtColor(pixel_array[::-1, :, [2, 1, 0]], cv2.COLOR_RGBA2RGB)

    def __del__(self):
        self.nemu.disconnect(self.handle)

    def screencap(self) -> cv2.Mat:
        result = self.nemu.capture_display(
            self.handle,
            self.display_id,
            self.buffer_size,
            ctypes.c_int(self.width),
            ctypes.c_int(self.height),
            self.pixels,
        )
        if result > 1:
            raise BufferError("截图错误")
        return self.__buffer2opencv()

    def screencap_raw(self) -> bytes:
        return self.screencap().tobytes()


if __name__ == '__main__':
    import time

    d = MuMuScreenCap(0, r"C:\Program Files\Netease\MuMu Player 12")
    s = time.time()
    np_arr = d.screencap()
    print((time.time() - s) * 1000)
    cv2.imshow("", np_arr)
    cv2.waitKey(0)
