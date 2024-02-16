"""
socket_file_transfer/receive.py
Main script handling receiving data.
"""

from socket_server import SocketServer

receive_instance = SocketServer(key=b"TestPassword1234", nonce=b"TestNonce1234567", receive=True, file="language.pdf")
print(receive_instance)
receive_instance.print_data()
receive_instance.receive_data()
