from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Blueprints
from .routes.instructor import instructor_bp
from .routes.program import programa_bp
from .routes.guide import guia_bp
from .routes.region import region_bp
from .routes.auth import auth_bp

def create_app():
    app = Flask(__name__)

    # App config
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "clave-super-secreta")

    # MongoDB config
    # MongoDB config
    mongodb_db = os.getenv("MONGODB_DB", "sgg_db")
    mongodb_host = os.getenv("MONGODB_URI", "mongodb://localhost:27017/sgg_db")
    
    connect(
        db=mongodb_db,
        host=mongodb_host,
        alias="default",
        uuidRepresentation='standard'
    )



    # Enable CORS for React development
    CORS(app, supports_credentials=True, origins=["http://localhost:3000", "http://127.0.0.1:3000"])

    # Register Blueprints
    app.register_blueprint(instructor_bp)
    app.register_blueprint(programa_bp)
    app.register_blueprint(guia_bp)
    app.register_blueprint(region_bp)
    app.register_blueprint(auth_bp)

    return app
