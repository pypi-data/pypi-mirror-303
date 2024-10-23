import json
import os.path
import socket
import subprocess
import threading

import cv2
import numpy as np
from adbutils import adb, adb_path
from loguru import logger

from msc.screencap import ScreenCap


class MiniCapStream:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.sock = None
        self.data = None
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.read_stream, daemon=True)
        self.data_available = threading.Condition()

    def start(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
        except ConnectionRefusedError:
            logger.error(
                f"Be sure to run `adb forward tcp:{self.port} localabstract:minicap`")
            return

        self.thread.start()

    def read_stream(self):
        banner = {
            'version': 0,
            'length': 0,
            'pid': 0,
            'realWidth': 0,
            'realHeight': 0,
            'virtualWidth': 0,
            'virtualHeight': 0,
            'orientation': 0,
            'quirks': 0
        }

        read_banner_bytes = 0
        banner_length = 2
        read_frame_bytes = 0
        frame_body_length = 0
        frame_body = bytearray()
        max_buf_size = 4096

        while not self.stop_event.is_set():
            chunk = self.sock.recv(max_buf_size)
            if not chunk:
                break

            # logger.info(f"chunk(length={len(chunk)})", )
            cursor = 0
            while cursor < len(chunk):
                if read_banner_bytes < banner_length:
                    if read_banner_bytes == 0:
                        banner['version'] = chunk[cursor]
                    elif read_banner_bytes == 1:
                        banner['length'] = banner_length = chunk[cursor]
                    elif 2 <= read_banner_bytes <= 5:
                        banner['pid'] += (chunk[cursor] <<
                                          ((read_banner_bytes - 2) * 8)) & 0xFFFFFFFF
                    elif 6 <= read_banner_bytes <= 9:
                        banner['realWidth'] += (chunk[cursor] <<
                                                ((read_banner_bytes - 6) * 8)) & 0xFFFFFFFF
                    elif 10 <= read_banner_bytes <= 13:
                        banner['realHeight'] += (chunk[cursor] <<
                                                 ((read_banner_bytes - 10) * 8)) & 0xFFFFFFFF
                    elif 14 <= read_banner_bytes <= 17:
                        banner['virtualWidth'] += (chunk[cursor] <<
                                                   ((read_banner_bytes - 14) * 8)) & 0xFFFFFFFF
                    elif 18 <= read_banner_bytes <= 21:
                        banner['virtualHeight'] += (chunk[cursor] <<
                                                    ((read_banner_bytes - 18) * 8)) & 0xFFFFFFFF
                    elif read_banner_bytes == 22:
                        banner['orientation'] = chunk[cursor] * 90
                    elif read_banner_bytes == 23:
                        banner['quirks'] = chunk[cursor]

                    cursor += 1
                    read_banner_bytes += 1

                    if read_banner_bytes == banner_length:
                        logger.info(f"banner {banner}", )
                else:
                    max_buf_size = frame_body_length
                    if len(chunk) - cursor >= frame_body_length:
                        frame_body.extend(chunk[cursor:cursor + frame_body_length])
                        with self.data_available:
                            self.data = frame_body
                            self.data_available.notify_all()  # 通知等待的线程
                        cursor += frame_body_length
                        read_frame_bytes = 0
                        frame_body_length = banner['virtualWidth'] * banner['virtualHeight'] * 4
                        frame_body = bytearray()
                    else:
                        frame_body.extend(chunk[cursor:])
                        frame_body_length -= len(chunk) - cursor
                        read_frame_bytes += len(chunk) - cursor
                        cursor = len(chunk)

    def stop(self):
        logger.info("Stopping the stream")
        self.stop_event.set()
        self.sock.close()
        self.thread.join()

    def next_image(self) -> bytes:
        with self.data_available:
            while self.data is None or len(self.data) == 0:
                self.data_available.wait()  # 等待数据可用
            return self.data


class MiniCapUnSupportError(Exception):
    pass


class MiniCap(ScreenCap):
    WORK_DIR = os.path.dirname(__file__)
    MINICAP_PATH = f"{WORK_DIR}/bin/minicap/libs"
    MINICAP_SO_PATH = f"{WORK_DIR}/bin/minicap/jni"
    MNC_HOME = "/data/local/tmp/minicap"
    MNC_SO_HOME = "/data/local/tmp/minicap.so"
    MINICAP_COMMAND = ["LD_LIBRARY_PATH=/data/local/tmp", "/data/local/tmp/minicap"]
    MINICAP_START_TIMEOUT = 3

    def __init__(
            self,
            serial: str,
            rate: int = None,
            quality: int = 100,
            skip_frame: bool = True,
            use_stream: bool = True
    ):
        """
        __init__ minicap截图方式

        Args:
            serial (str): 设备id
            rate (int, optional): 截图帧率. Defaults to 自动获取.
            quality (int, optional): 截图品质1~100之间. Defaults to 100.
            skip_frame(bool,optional): 当无法快速获得截图时，跳过这个帧
            use_stream (bool, optional): 是否使用stream的方式. Defaults to True.
        """
        # 初始化对象
        self.adb = adb.device(serial)
        self.skip_frame = skip_frame
        self.use_stream = use_stream
        self.quality = quality
        self.rate = rate
        # 初始化设备信息
        self.rotation = None
        self.vm_size = None
        self.port = None
        self.abi = self.adb.getprop("ro.product.cpu.abi")
        self.sdk = self.adb.getprop("ro.build.version.sdk")
        # 获取截图字节数据长度
        self.width, self.height = self.adb.window_size()
        self.buffer_size = self.width * self.height * 4

        self.kill()  #杀掉minicap进程
        self.install()  #安装minicap
        self.get_device_input_info()  #使用minicap -i获取一些参数信息
        # 启动minicap stream
        if self.use_stream:
            self.popen = None
            self.stream = None
            self.start_minicap_by_stream()

    def kill(self):
        self.adb.shell(['pkill', '-9', 'minicap'])

    def install(self):
        """安装minicap"""
        if str(self.sdk) == "32" and str(self.abi) == "x86_64":
            self.abi = "x86"
        if int(self.sdk) > 34:
            raise MiniCapUnSupportError("minicap does not support Android 12+")
        self.adb.sync.push(f"{self.MINICAP_PATH}/{self.abi}/minicap", self.MNC_HOME)
        self.adb.sync.push(
            f"{self.MINICAP_SO_PATH}/android-{self.sdk}/{self.abi}/minicap.so", self.MNC_SO_HOME
        )
        self.adb.shell(["chmod +x", self.MNC_HOME])

    def get_device_input_info(self):
        try:
            # 通过 -i 参数获取屏幕信息
            command = self.MINICAP_COMMAND + ["-i"]
            info_result = self.adb.shell(command)
            # 找到JSON数据的起始位置
            start_index = info_result.find('{')
            # 提取JSON字符串
            if start_index != -1:
                extracted_json = info_result[start_index:]
                logger.info(extracted_json)
            else:
                raise MiniCapUnSupportError("minicap does not support")
            info = json.loads(extracted_json)
            self.vm_size = self.adb.shell("wm size").split(" ")[-1]
            self.rotation = info.get("rotation")
            self.rate = info.get("fps") if self.rate is None else self.rate
        except Exception as e:
            raise MiniCapUnSupportError("minicap does not support")

    def start_minicap(self):
        adb_command = [adb_path(), "-s", self.adb.serial, "shell"]
        adb_command.extend(self.MINICAP_COMMAND)
        adb_command.extend(["-P", f"{self.vm_size}@{self.vm_size}/{self.rotation}"])
        adb_command.extend(["-Q", str(self.quality)])
        adb_command.extend(["-r", str(self.rate)])
        if self.skip_frame:
            adb_command.extend(["-S"])
        logger.info(adb_command)
        # 启动minicap popen
        self.popen = subprocess.Popen(
            adb_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        logger.info("minicap connection takes a long time, please be patient.")
        time.sleep(self.MINICAP_START_TIMEOUT)

    def forward_port(self):
        self.port = self.adb.forward_port("localabstract:minicap")

    def read_minicap_stream(self):
        # 会通过adb转发到本地端口，所以地址写死为127.0.0.1，端口号为转发得到的端口号
        self.stream = MiniCapStream("127.0.0.1", self.port)
        self.stream.start()

    def start_minicap_by_stream(self):
        self.start_minicap()
        self.forward_port()
        self.read_minicap_stream()

    def stop_minicap_by_stream(self):
        if self.use_stream:
            self.stream.stop()  # 停止stream
            if self.popen.poll() is None:  # 清理管道
                self.popen.kill()

    def __del__(self):
        self.stop_minicap_by_stream()

    def get_minicap_frame(self) -> bytes:
        adb_command = self.MINICAP_COMMAND + []
        adb_command.extend(
            ["-P", f"{self.vm_size}@{self.vm_size}/{self.rotation}"])
        adb_command.extend(["-Q", str(self.quality)])
        adb_command.extend(["-s"])
        raw_data = self.adb.shell(adb_command, encoding=None)
        jpg_data = raw_data.split(b"for JPG encoder\n")[-1]
        return jpg_data

    def screencap_raw(self) -> bytes:
        if self.use_stream:
            return self.stream.next_image()
        else:
            return self.get_minicap_frame()

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

    d = MiniCap(serial="127.0.0.1:16384")

    for i in range(10):
        s = time.time()
        np_arr = d.screencap()
        print((time.time() - s) * 1000)
        time.sleep(0.5)
    cv2.imshow("", np_arr)
    cv2.waitKey(0)
