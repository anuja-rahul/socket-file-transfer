"""
socket_file_transfer/cryptography.py
Main script for encrypting/decrypting data.
"""

import uuid
from Crypto.Cipher import AES
from python_datalogger import DataLogger


class CryptoHandler:
    def __init__(self, key: bytes, nonce: bytes):
        self.__logger = DataLogger(name=f"CryptoHandler__{uuid.uuid4()}__", level="DEBUG", propagate=False)
        self.__key = key
        self.__nonce = nonce
        self.__cipher = self.__get_cipher()

    def __get_cipher(self):
        self.__logger.log_info("called CryptoHandler__get_cipher")
        return AES.new(self.__key, AES.MODE_EAX, self.__nonce)

    def encrypt(self, data: bytes) -> bytes:
        self.__logger.log_info("called CryptoHandler__encrypt")
        return self.__cipher.encrypt(data)

    def decrypt(self, data: bytes) -> bytes:
        self.__logger.log_info("called CryptoHandler__decrypt")
        return self.__cipher.decrypt(data)
