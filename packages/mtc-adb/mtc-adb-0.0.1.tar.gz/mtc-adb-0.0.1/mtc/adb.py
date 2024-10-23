from typing import List

from adbutils import adb
from mcore import Point

from mtc.touch import Touch


class ADBTouch(Touch):
    def __init__(self, serial) -> None:
        """
        __init__ ADB 操作方式

        Args:
            serial (str): 设备id
        """
        self.__adb = adb.device(serial)

    def click(self, point: Point, duration: int = 100):
        adb_command = ["input", "touchscreen", "swipe"]
        x, y = point.x, point.y
        adb_command.extend([str(x), str(y), str(x), str(y), str(duration)])
        self.__adb.shell(adb_command)

    def swipe(self, points: List[Point], duration: int = 500):
        start_x, start_y = points[0].x, points[0].y
        end_x, end_y = points[-1].x, points[-1].y
        self.__adb.swipe(start_x, start_y, end_x, end_y, duration / 1000)
