It's Working barely !!!    


```python

# To get started you need to have 2 directories called "send" and "receive"
# on your working directory

# You can either create them manually or you can call for an empty object 
# from either SocketServer or SocketClient
# which will generate the required directories and test files.

"""
Example:
    ../send.py
"""

from socket_client import SocketClient

sample = SocketClient()

# make sure to remove any test objects before instantiating either
# the working server or client objects because the singleton design will only allow 
# one instance/object  per class from both SocketServer and SocketClient.

# in case of an unknown error check your log file from (./logs)
# they will most likely contain the type of the error, name of the method in which 
# the said error originated and the time of the error.

```
