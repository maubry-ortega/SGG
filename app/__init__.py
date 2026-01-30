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
from .routes.guia_list import guide_list_bp

def create_app():
    app = Flask(__name__)

    # App config
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "clave-super-secreta")

    # MongoDB config
    connect(
        db=os.getenv("MONGODB_DB", "sgg_db"),
        host=os.getenv("MONGODB_URI", "mongodb://localhost:27017/sgg_db"),
        alias="default"
    )

    # Enable CORS
    CORS(app, supports_credentials=True)

    # Register Blueprints
    app.register_blueprint(instructor_bp)
    app.register_blueprint(programa_bp)
    app.register_blueprint(guia_bp)
    app.register_blueprint(region_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(guide_list_bp)

    return app
