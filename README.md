It's Working barely !!!    

```
receive.py(server) must be running before send.py(client) to establish a connection.
if not, it will most likely return a WinError-10061 (on windows).

To get started you need to have 2 directories called "send" and "receive"
on your working directory

You can either create them manually or you can call for an empty object 
from either SocketServer or SocketClient
which will generate the required directories and test files.

make sure to remove any test objects before instantiating either
the working server or client objects because the singleton design will only allow 
one instance/object  per class from both SocketServer and SocketClient.

in case of an unknown error check your log file from (./logs)
they will most likely contain the type of the error, name of the method in which 
the said error originated and the time of the error.
```


```python
"""
client for sending the files
socket-file-transfer/send.py
"""

from socket_client import SocketClient

sample = SocketClient(key=b"TestPassword1234", nonce=b"TestNonce1234567", send=True, file="filename.extension")

# param: nonce,key (both key and nonce will only accept exactly 16 characters of bytes)
# param: send (send must be True before calling the send_data() method)
# param: file (file must be the name(with extension) of the file in the send folder which you intend to send.)
```
```python
"""
server for receiving the files
socket-file-transfer/receive.py
"""

from socket_server import SocketServer

receive_instance = SocketServer(key=b"TestPassword1234", nonce=b"TestNonce1234567", receive=True, file="vid.mp4")

# param: nonce,key (both key and nonce will only accept exactly 16 characters of bytes)
# param: receive (send must be True before calling the receive_data() method)
# param: file (file must be the name(with extension) of the file which you intend to receive from the client.)
```
