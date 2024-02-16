"""
socket_file_transfer/send.py
Main script handling sending data.
"""

from socket_client import SocketClient


send_instance = SocketClient(key=b"TestPassword1234", nonce=b"TestNonce1234567", send=True, file="vid.mp4")
# print(send_instance)
# send_instance.print_data()
send_instance.send_data()
