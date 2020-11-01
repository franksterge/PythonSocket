import socket
from constants.constants import ServerKeys, ServerConstants

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(ServerConstants.HEADER_LENGTH)
        if not len(message_header):
            print("message_header is None")
        message_length = int(message_header.decode(ServerConstants.DECODE_VALUE).strip())
        result = {
            ServerKeys.HEADER: message_header,
            ServerKeys.DATA: client_socket.recv(message_length)
        }
        return result
    except:
        return False
