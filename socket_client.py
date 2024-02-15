"""
socket_file_transfer/socket_client.py
Main script for accessing the client classes.
"""

from abc import ABCMeta, abstractmethod, ABC


class ISocketClient(metaclass=ABCMeta):
    @abstractmethod
    def get_data(self):
        """Implemented in child class"""


class SocketClient(ISocketClient, ABC):
    __instance = None

    @staticmethod
    def get_instance():
        if SocketClient.__instance is None:
            SocketClient(password="root", nonce="nonce")
        return SocketClient.__instance

    def __init__(self, password, nonce, send: bool = False):
        if SocketClient.__instance is not None:
            raise Exception("Cannot be instantiated more than once")

        self.__password = password
        self.__nonce = nonce
        self.__send = send
