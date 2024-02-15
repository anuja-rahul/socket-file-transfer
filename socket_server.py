"""
socket_file_transfer/socket_client.py
Main script for accessing the server classes.
"""

from abc import ABCMeta, abstractmethod, ABC

# TODO: Add socket server functionality


class ISocketServer(metaclass=ABCMeta):
    @abstractmethod
    def print_data(self):
        """Implemented in child class"""


class SocketServer(ISocketServer, ABC):
    __instance = None

    @staticmethod
    def get_instance():
        if SocketServer.__instance is None:
            SocketServer(password="root", nonce="nonce")
        return SocketServer.__instance

    def __init__(self, password, nonce, receive: bool = False):
        if SocketServer.__instance is not None:
            raise Exception("Cannot be instantiated more than once")
        else:
            self.__password = password
            self.__nonce = nonce
            self.__receive = receive
            SocketServer.__instance = self


