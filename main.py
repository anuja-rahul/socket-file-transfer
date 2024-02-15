"""
socket_file_transfer/main.py
Main script for accessing the handler class.
"""

from socket_client import SocketClient

instance = SocketClient(key=b"TestPassword1234", nonce=b"TestNonce1234567", send=True, file="test.txt")
print(instance)
