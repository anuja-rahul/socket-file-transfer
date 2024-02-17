"""
socket_file_transfer/socket_client.py
Main script for sending(client) data.
"""

import os
import socket
from datetime import datetime
from abc import ABCMeta, abstractmethod, ABC

from validator import Validator
from init_handler import InitEnv
from cryptography import CryptoHandler
from python_datalogger import DataLogger


class ISocketClient(metaclass=ABCMeta):
    @abstractmethod
    def print_data(self):
        """Implemented in child class"""


class SocketClient(ISocketClient, ABC):
    __instance = None

    @staticmethod
    def get_instance():
        if SocketClient.__instance is None:
            SocketClient(key=b"SocketClientsPWD", nonce=b"SocketClientsNCE", file="test.txt")
        return SocketClient.__instance

    def __init__(self, key: bytes = b'DefaultSampleKey', nonce: bytes = b'DefaultSampleNCE',
                 send: bool = False, file: str = "test.txt"):
        InitEnv.init_env()
        self.__logger = DataLogger(name="SocketClient", propagate=True, level="DEBUG")

        if SocketClient.__instance is not None:
            raise Exception("Cannot be instantiated more than once")
        else:
            self.__key = key
            self.__nonce = nonce
            self.__send = send
            self.__file = f"send/{file}"
            self.__validator = Validator(key=self.__key, nonce=self.__nonce, file=self.__file)
            self.__hashes = self.__validator.get_hashes()
            self.__client = self.__get_client()
            self.__cipher = CryptoHandler(key=self.__key, nonce=self.__nonce)

            if self.__validator.validate_length():
                self.__validity = True
            else:
                raise Exception("\nPassword and Nonce must be exactly 16 characters long !\n")

            SocketClient.__instance = self

    @staticmethod
    def print_data(**kwargs):
        print(SocketClient.__instance.__send)

    @staticmethod
    @DataLogger.logger
    def __get_client():
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @DataLogger.logger
    def send_data(self, port: int = 8999):
        if self.__send:

            self.__client.connect(('localhost', port))

            if self.__validator.check_file() and self.__validity:

                with open(self.__file, 'rb') as f:
                    data = f.read()

                file_size = os.path.getsize(self.__file)
                encrypted_data = self.__cipher.encrypt(data)

                self.__client.send(self.__file.split("/")[-1].encode())
                self.__logger.log_info(f"Sent file name - {datetime.now().time()} : "
                                       f"({self.__file.split("/")[-1]})")

                self.__client.send(str(file_size).encode())
                self.__logger.log_info(f"Sent file size - {datetime.now().time()} : ({file_size}B)")

                self.__client.send(str(self.__hashes).encode())
                self.__logger.log_info(f"Sent hashes - {datetime.now().time()}")

                self.__client.sendall(encrypted_data)
                self.__client.send(b"<END>")
                self.__logger.log_info(f"End of data packets - {datetime.now().time()}\n")

            else:
                raise Exception("\nFile not found or check your key again !\n")

            self.__client.close()

        else:
            self.__logger.log_critical("(send) parameter must be True to call this method")

    def __repr__(self):
        return f"{self.__hashes}"
