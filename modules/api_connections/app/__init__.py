from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from app.config import config_by_name
from app.routes import register_routes
    
db = SQLAlchemy()

def create_app(env=None):
    '''
        Initialize the Flask app as an api by using the 'flask-restx' library.
        Registers all the related routes to the api and the return the initialized flask object 
    '''
    
    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect API", version="0.1.0")

    CORS(app)

    register_routes(api)
    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app