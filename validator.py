"""
socket_file_transfer/validator.py
Main script for validating data.
"""

import uuid
import hashlib


class Validator:
    def __init__(self, password: bytes = None, nonce: bytes = None, file: str = None):
        self.__request = uuid.uuid4()
        self.__password = password
        self.__nonce = nonce
        self.file = file

    def validate_length(self):
        if self.__password and self.__nonce:
            if len(self.__password) != 16 or len(self.__nonce) != 16:
                return False
            else:
                return True

    # noinspection PyTypeChecker
    def get_hashes(self):
        pwd_hash = None
        nonce_hash = None
        file_hash = None

        if self.__password and self.__nonce:
            pwd_hash = hashlib.sha256(self.__password)
            nonce_hash = hashlib.sha256(self.__nonce)

        try:
            if self.file:
                with open(self.file, 'rb') as file:
                    file_hash = hashlib.file_digest(file, "sha256").hexdigest()
        except FileNotFoundError:
            raise Exception("\nAdd a valid file name in the send/receive folder !\n")

        return {"password_hash": pwd_hash, "nonce_hash": nonce_hash, "file_hash": file_hash}
