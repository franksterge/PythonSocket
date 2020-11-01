import socket
import select
from server import server_socket, receive_message
from constants.constants import ServerKeys, ServerConstants


sockets_list = [server_socket]
clients = {}
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((ServerConstants.IP, ServerConstants.PORT))
server_socket.listen()
print('server side is running')
while True:
    read_sockets, write_sockets, exception_sockets = select.select(sockets_list, [], sockets_list)

    print('{} read clients are online'.format((len(read_sockets) - 1)))
    print('{} write clients are online'.format((len(write_sockets) - 1)))
    print('{} exception clients are online'.format((len(exception_sockets) - 1)))
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            print('here')
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user == False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(user.get(ServerKeys.DATA) + 'joined')
        else:
            message = receive_message(notified_socket)
            if message == False:
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]

            # prints out message received
            print('received message from {}: {}'.format(user.get(ServerKeys.DATA).decode(ServerConstants.DECODE_VALUE),
                                                        message.get(ServerKeys.DATA).decode(ServerConstants.DECODE_VALUE)))

            for client_socket in clients.keys():
                if client_socket != notified_socket:
                    client_socket.send(user.get(ServerKeys.HEADER) + user.get(ServerKeys.DATA) +
                                       message.get(ServerKeys.HEADER) + message.get(ServerKeys.DATA))

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
