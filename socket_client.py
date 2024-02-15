"""
socket_file_transfer/socket_client.py
Main script for sending(client) data.
"""

import os
import socket
from abc import ABCMeta, abstractmethod, ABC

from validator import Validator
from init_handler import InitEnv
from cryptography import AESHandler


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

    def __init__(self, file: str, key: bytes, nonce: bytes, send: bool = False):
        InitEnv.init_env()

        if SocketClient.__instance is not None:
            raise Exception("Cannot be instantiated more than once")
        else:
            self.__key = key
            self.__nonce = nonce
            self.__send = send
            self.__file = f"send/{file}"
            self.__validator = Validator(key=key, nonce=nonce, file=file)
            self.__hashes = self.__validator.get_hashes
            self.__client = self.__get_client()
            self.__cipher = AESHandler(key=self.__key, nonce=self.__nonce)

            if self.__validator.validate_length():
                self.__validity = True
            else:
                raise Exception("\nPassword and Nonce must be exactly 16 characters long !\n")

            SocketClient.__instance = self

    @staticmethod
    def print_data(**kwargs):
        print(f"({SocketClient.__instance.send})")

    @staticmethod
    def __get_client():
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __send_data(self, port: int = 8999):
        self.__client.connect(('localhost', port))

        if self.__validator.check_file():
            with open(self.__file, 'rb') as f:
                data = f.read()
            file_size = os.path.getsize("language.pdf")
            encrypted_data = self.__cipher.encrypt(data)
            self.__client.send(self.__file.split("/")[-1].encode())
            self.__client.send(str(file_size).encode())
            self.__client.send(str(self.__hashes).encode())
            self.__client.sendall(encrypted_data)
            self.__client.send(b"<END>")
            self.__client.close()

        else:
            raise Exception("\nFile not found !\n")

    def __repr__(self):
        return f"({self.__key}, {self.__nonce}, {self.__send})"
