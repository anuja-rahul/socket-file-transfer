"""
socket_file_transfer/socket_client.py
Main script for accessing the server classes.
"""

import tqdm
import ast
import socket
from abc import ABCMeta, abstractmethod, ABC

from validator import Validator
from init_handler import InitEnv
from cryptography import AESHandler


class ISocketServer(metaclass=ABCMeta):
    @abstractmethod
    def print_data(self):
        """Implemented in child class"""


class SocketServer(ISocketServer, ABC):
    __instance = None

    @staticmethod
    def get_instance():
        if SocketServer.__instance is None:
            SocketServer(key=b"SocketClientsPWD", nonce=b"SocketClientsNCE", file="test.txt")
        return SocketServer.__instance

    def __init__(self, key, nonce, receive: bool = False, file: str = "test.txt"):
        InitEnv.init_env()

        if SocketServer.__instance is not None:
            raise Exception("Cannot be instantiated more than once")
        else:
            self.__key = key
            self.__nonce = nonce
            self.__receive = receive
            self.__file = f"receive/{file}"
            self.__validator = Validator(key=self.__key, nonce=self.__nonce, file=self.__file)
            self.__hashes = self.__validator.get_hashes()
            self.__server = self.__get_server()
            self.__cipher = AESHandler(key=self.__key, nonce=self.__nonce)
            self.__progress = None

            if self.__validator.validate_length():
                self.__validity = True
            else:
                raise Exception("\nPassword and Nonce must be exactly 16 characters long !\n")

            SocketServer.__instance = self

    @staticmethod
    def print_data(**kwargs):
        print(SocketServer.__instance.__receive)

    @staticmethod
    def __get_server():
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @staticmethod
    def __get_progress(file_size: str):
        return tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=float(file_size))

    def receive_data(self, port: int = 8999):
        self.__server.bind(('localhost', port))
        self.__server.listen()
        client, addr = self.__server.accept()

        if self.__validator.check_file() and self.__validity:
            file_name = client.recv(1024).decode()
            file_size = client.recv(1024).decode()
            hashes = client.recv(1024).decode()
            new_hash = ast.literal_eval(hashes)

            if self.__validator.check_hashes(hashes=new_hash):
                self.__progress = self.__get_progress(file_size=file_size)
                file = open(f"receive/{file_name}", 'wb')
                done = False
                file_bytes = b""

                while not done:
                    data = client.recv(1024)
                    if data[-5:] == b"<END>":
                        done = True
                    else:
                        file_bytes += data
                        self.__progress.update(1024)

                file.write(self.__cipher.decrypt(file_bytes[:-5]))
                file.close()
            else:
                print("\nHashes of the received key and nonce does not match the "
                      "hashes of the key and nonce your entered !\n")

        client.close()
        self.__server.close()

    def __repr__(self):
        return f"{self.__hashes}"
