"""
socket_file_transfer/validator.py
Main script for validating data.
"""
import os
import uuid
import hashlib
from python_datalogger import DataLogger


class Validator:
    def __init__(self, key: bytes = None, nonce: bytes = None, file: str = None):
        self.__logger = DataLogger(name=f"Validator__{uuid.uuid4()}__", level="DEBUG", propagate=True)
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
    """
    def check_file(self):
        send_samples = os.listdir("send")
        recv_samples = os.listdir("receive")

        if self.file.split("/")[-1] in send_samples or self.file in recv_samples:
            return True
        else:
            return False
    """
    # noinspection PyTypeChecker
    def get_hashes(self) -> dict[str:bytes]:
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
            # print("\nAdd a valid file name in the send/receive folder !\n")
            pass

        return {"key_hash": key_hash, "nonce_hash": nonce_hash, "file_hash": file_hash}

    @DataLogger.logger
    def check_hashes(self, hashes: dict[str:bytes]):
        local_key_hash = self.get_hashes()["key_hash"]
        local_nonce_hash = self.get_hashes()["nonce_hash"]
        foreign_key_hash = hashes["key_hash"]
        foreign_nonce_hash = hashes["nonce_hash"]

        if local_key_hash == foreign_key_hash and local_nonce_hash == foreign_nonce_hash:
            self.__logger.log_info("[key,nonce] hash verified successfully\n")
            return True

        else:
            self.__logger.log_warning("[key,nonce] hash verification failed")
            return False
