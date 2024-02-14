"""
socket_file_transfer/socket_handler.py
Main script for accessing the client and server classes.
"""

from abc import ABCMeta, abstractmethod, ABC


class ISocketHandler(metaclass=ABCMeta):
    @abstractmethod
    def get_data(self):
        """Implemented in child class"""


class SocketHandler(ISocketHandler, ABC):
    __instance = None

    @staticmethod
    def get_instance():
        if SocketHandler.__instance is None:
            SocketHandler(password="root", nonce="nonce")
        return SocketHandler.__instance

    def __init__(self, password, nonce, send: bool = False, receive: bool = False):
        if SocketHandler.__instance is not None:
            raise Exception("Cannot be instantiated more than once")

        self.__password = password
        self.__nonce = nonce
        self.__send = send
        self.__receive = receive
