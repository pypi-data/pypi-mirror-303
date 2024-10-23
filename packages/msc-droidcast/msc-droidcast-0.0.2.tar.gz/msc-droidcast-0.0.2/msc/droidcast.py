import os.path
import subprocess

import cv2
import numpy as np
import requests
from adbutils import adb, adb_path
from loguru import logger

from msc.screencap import ScreenCap


class DroidCast(ScreenCap):
    APK_PACKAGE_NAME = "com.rayworks.droidcast"
    PM_PATH_SHELL = f"pm path {APK_PACKAGE_NAME}"
    START_CMD = f"exec app_process / {APK_PACKAGE_NAME}.Main"
    APK_NAME_PREFIX = "DroidCast_"
    APK_VERSION = "1.4.1"
    APK_PATH = f"{os.path.dirname(__file__)}/bin/{APK_NAME_PREFIX}{APK_VERSION}.apk"
    APK_ANDROID_PATH = f"/data/local/tmp/{APK_NAME_PREFIX}{APK_VERSION}.apk"

    def __init__(self, serial: str, display_id: int = None, port: int = 53516, timeout: int = 3):
        """
        __init__ DroidCast截图方法

        Args:
            serial (str): 设备id
            display_id (int): 显示器id use `adb shell dumpsys SurfaceFlinger --display-id` to get
            port (int): 设备上DroidCast监听端口号
            timeout (int): 请求DroidCast截图最长时间
        """
        self.adb = adb.device(serial)
        self.display_id = display_id
        self.remote_port = port
        self.timeout = timeout
        # 初始化默认变量
        self.session = requests.Session()
        self.popen = None
        self.local_port = None
        self.url = None
        # 获取截图字节流大小
        self.width, self.height = self.adb.window_size()
        self.buffer_size = self.width * self.height * 4
        # 试安装并启动DroidCast
        self.install()
        self.start()

    def install(self):
        if self.APK_PACKAGE_NAME not in self.adb.list_packages():
            self.adb.install(self.APK_PATH, nolaunch=True)
        else:
            if self.adb.package_info(self.APK_PACKAGE_NAME)['version_name'] != self.APK_VERSION:
                self.adb.uninstall(self.APK_PACKAGE_NAME)
                self.adb.install(self.APK_PATH, nolaunch=True)

    def open_popen(self):
        class_path = "CLASSPATH=" + self.adb.shell(self.PM_PATH_SHELL).split(":")[1]  # 获取apk的classpath
        # 配置命令
        adb_command = [adb_path(), "-s", self.adb.serial,
                       "shell", class_path, self.START_CMD]
        adb_command.extend([f"--port={self.remote_port}"])
        if self.display_id:
            adb_command.extend([f"--display_id={self.display_id}"])
        logger.info(adb_command)
        # 启动
        self.popen = subprocess.Popen(
            adb_command,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )

    def forward_port(self):
        self.local_port = self.adb.forward_port(self.remote_port)
        self.url = f"http://localhost:{self.local_port}/screenshot?format=raw"

    def start(self):
        self.open_popen()
        self.forward_port()
        self.screencap_raw()
        logger.info("DroidCast启动完成")

    def stop(self):
        if self.popen.poll() is None:
            self.popen.kill()  # 关闭管道

    def __del__(self):
        self.stop()

    def screencap_raw(self) -> bytes:
        try:
            return self.session.get(self.url, timeout=self.timeout).content
        except requests.exceptions.ConnectionError:
            self.stop()
            self.start()
            return self.screencap_raw()

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

