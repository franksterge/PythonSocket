# handles user creation connecting to db
from constants.constants import UserKeys, ServerConstants

class ClientService:


    def create_user_client(self, user_dict, client_socket):
        '''
        : Creates a user client service based on the user_dict passed in.
        :
        : Returns confirmation
        :
        '''
        user_name = user_dict.get(UserKeys.NAME)
        user_name_header = '{}'.format(len(user_name))
        client_socket.client_socket.send(user_name_header.encode(ServerConstants.DECODE_VALUE) + user_name.encode(ServerConstants.DECODE_VALUE))
        print(user_name + ' is joining the server')


