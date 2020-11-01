import socket
from constants.constants import ServerConstants, ServerKeys,UserKeys

class ClientSocket:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ServerConstants.IP, ServerConstants.PORT))
        self.client_socket.setblocking(False)

