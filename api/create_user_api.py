from flask import Blueprint, request, jsonify
from constants.constants import UserKeys
from services import client_service
from client.client_socket import ClientSocket

CREATE_USER_API = Blueprint('create_user_api', __name__)

@CREATE_USER_API.route('/create_user', methods=['POST'])
def create_user():
    '''
    : creates a user client based on the given user dict
    '''
    user_dict = request.get_json().get(UserKeys.USER)
    client_socket = ClientSocket()
    client_service.create_user_client(user_dict, client_socket)
    return jsonify(user_dict)
