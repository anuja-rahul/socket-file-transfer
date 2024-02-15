"""
socket_file_transfer/cryptography.py
Main script for encrypting/decrypting data.
"""

from Crypto.Cipher import AES


class AESHandler:
    def __init__(self, key: bytes, nonce: bytes):
        self.__key = key
        self.__nonce = nonce
        self.__cipher = self.__get_cipher()

    def __get_cipher(self):
        return AES.new(self.__key, AES.MODE_EAX, self.__nonce)

    def encrypt(self, data: bytes) -> bytes:
        return self.__cipher.encrypt(data)

