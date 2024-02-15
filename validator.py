"""
socket_file_transfer/validator.py
Main script for validating data.
"""
import os
import uuid
import hashlib


class Validator:
    def __init__(self, key: bytes = None, nonce: bytes = None, file: str = None):
        self.__request = uuid.uuid4()
        self.__key = key
        self.__nonce = nonce
        self.file = file

    def validate_length(self):
        if self.__key and self.__nonce:
            if len(self.__key) != 16 or len(self.__nonce) != 16:
                return False
            else:
                return True

    def check_file(self):
        send_samples = os.listdir("send")
        recv_samples = os.listdir("receive")

        if self.file in send_samples or self.file in recv_samples:
            return True
        else:
            return False

    # noinspection PyTypeChecker
    def get_hashes(self):
        key_hash = None
        nonce_hash = None
        file_hash = None

        if self.__key and self.__nonce:
            key_hash = hashlib.sha256(self.__key).hexdigest()
            nonce_hash = hashlib.sha256(self.__nonce).hexdigest()

        try:
            if self.file:
                with open(self.file, 'rb') as file:
                    file_hash = hashlib.file_digest(file, "sha256").hexdigest()
        except FileNotFoundError:
            raise Exception("\nAdd a valid file name in the send/receive folder !\n")

        return {"key_hash": key_hash, "nonce_hash": nonce_hash, "file_hash": file_hash}
