"""
socket_file_transfer/main.py
Main script for accessing the handler class.
"""

from socket_handler import SocketSender

instance = SocketSender(password="TestPassword1234", nonce="TestNonce1234567")
