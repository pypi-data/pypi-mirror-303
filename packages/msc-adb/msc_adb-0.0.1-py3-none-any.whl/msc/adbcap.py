import subprocess

import cv2
import numpy as np
from adbutils import adb, adb_path

from msc.screencap import ScreenCap


def _run_adb_command(command) -> bytes:
    """
      执行ADB命令并返回结果。

      :param command: ADB命令列表
      :return: 命令的输出字节数据
      """
    try:
        with subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ) as process:
            data, err = process.communicate(timeout=10)

        if process.returncode == 0 and data:
            return data
        else:
            raise subprocess.TimeoutExpired(None, timeout=10, stderr=err)
    except subprocess.TimeoutExpired as e:
        raise e
    except Exception as e:
        raise RuntimeError(f"Error while running ADB command: {e} (stderr: {err})")


class ADBCap(ScreenCap):
    def __init__(self, serial: str, display_id: int = None):
        """
          __init__ ADB 截图方式

          Args:
              serial (str): 设备id
          """
        self.adb = adb.device(serial)
        self.display_id = display_id
        self.width, self.height = self.adb.window_size()
        # 计算预期的数据长度
        self.buffer_size = self.width * self.height * 4

    def screencap_raw(self) -> bytes:
        """
          截图并以字节流的形式返回Android设备的屏幕。

          :return: 截图的字节数据。
          """
        adb_command = [adb_path(), "-s", self.adb.serial, "exec-out", "screencap"]
        if self.display_id:
            adb_command.extend(["-d", str(self.display_id)])
        return _run_adb_command(adb_command)

    def screencap(self) -> cv2.Mat:
        # 获取原始屏幕截图数据
        raw = self.screencap_raw()

        # 检查实际数据长度是否符合预期
        if len(raw) < self.buffer_size:
            raise ValueError(f"Raw data length {len(raw)} is less than expected {self.buffer_size}")

        # 将原始数据转换为 NumPy 数组
        arr = np.frombuffer(raw[:self.buffer_size], np.uint8).reshape((self.height, self.width, 4))

        # 将 RGBA 格式转换为 BGR 格式
        return cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)


if __name__ == '__main__':
    import time

    d = ADBCap(serial="127.0.0.1:16384")
    s = time.time()
    np_arr = d.screencap()
    print((time.time() - s) * 1000)
    cv2.imshow("", np_arr)
    cv2.waitKey(0)
