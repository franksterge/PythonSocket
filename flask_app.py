from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
import traceback
from constants.constants import ServerConstants
from constants.error_lib import InternalException
from api import crate_app, socketio

application = crate_app()

@application.route('/', methods=['GET'])
def home():
    return 'Welcome to code breakers'

@application.errorhandler(InternalException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@application.errorhandler(Exception)
def handle_error(e):
    print('handling error')
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    print(traceback.format_exc())

    return jsonify(error='Internal Server Error'), 500

if __name__ == "__main__":
    socketio.run(application, host=ServerConstants.IP, debug=True, port=8080)
