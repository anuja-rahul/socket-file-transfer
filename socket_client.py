"""
socket_file_transfer/socket_client.py
Main script for accessing the client classes.
"""

from abc import ABCMeta, abstractmethod, ABC

from validator import Validator
from init_handler import InitEnv


class ISocketClient(metaclass=ABCMeta):
    @abstractmethod
    def print_data(self):
        """Implemented in child class"""


class SocketClient(ISocketClient, ABC):
    __instance = None

    @staticmethod
    def get_instance():
        if SocketClient.__instance is None:
            SocketClient(password=b"SocketClientsPWD", nonce=b"SocketClientsNCE", file="test.txt")
        return SocketClient.__instance

    def __init__(self, file: str, password: bytes, nonce: bytes, send: bool = False):
        InitEnv.init_env()

        if SocketClient.__instance is not None:
            raise Exception("Cannot be instantiated more than once")
        else:
            self.__password = password
            self.__nonce = nonce
            self.__send = send
            self.__file = file
            self.__validator = Validator(password=password, nonce=nonce, file=file)
            self.__hashes = self.__validator.get_hashes

            if self.__validator.validate_length():
                self.__validity = True
            else:
                raise Exception("\nPassword and Nonce must be exactly 16 characters long !\n")

            SocketClient.__instance = self

    @staticmethod
    def print_data(**kwargs):
        print(f"({SocketClient.__instance.send})")

    def __repr__(self):
        return f"({self.__password}, {self.__nonce}, {self.__send})"
