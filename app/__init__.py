# app/__init__.py
from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Blueprints
from .routes.instructor import instructor_bp
from .routes.program import programa_bp
from .routes.guide import guia_bp
from .routes.region import region_bp
from .routes.auth import auth_bp

def create_app():
    app = Flask(__name__)

    # Configuración general
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "clave-super-secreta")

    # MongoDB
    connect(
        db=os.getenv("MONGODB_DB", "sgg_db"),
        host=os.getenv("MONGODB_URI", "mongodb://localhost:27017/sgg_db"),
        alias="default"
    )

    # CORS
    CORS(app, supports_credentials=True)

    # Registro de Blueprints
    app.register_blueprint(instructor_bp, url_prefix="/api/instructores")
    app.register_blueprint(programa_bp, url_prefix="/api/programas")
    app.register_blueprint(guia_bp, url_prefix="/api/guias")
    app.register_blueprint(region_bp, url_prefix="/api/regiones")
    app.register_blueprint(auth_bp)

    return app
