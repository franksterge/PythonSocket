from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from api.create_user_api import CREATE_USER_API

socketio = SocketIO()
def crate_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    CORS(app)
    app.register_blueprint(CREATE_USER_API, url_prefix='/api/create_user')
    socketio.init_app(app)
    return app