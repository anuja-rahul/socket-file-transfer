"""
socket_file_transfer/main.py
Main script for accessing the handler class.
"""

from socket_client import SocketClient
from socket_server import SocketServer

receive_instance = SocketServer(key=b"TestPassword1234", nonce=b"TestNonce1234567", receive=True, file="test.txt")
print(receive_instance)
receive_instance.print_data()

send_instance = SocketClient(key=b"TestPassword1234", nonce=b"TestNonce1234567", send=True, file="test.txt")
print(send_instance)
send_instance.print_data()
