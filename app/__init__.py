from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Blueprints
from .routes.instructor import instructor_bp
from .routes.program import programa_bp
from .routes.guide import guia_bp

def create_app():
    app = Flask(__name__)

    # Configuración básica de Flask
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "clave-super-secreta")

    # Conexión a MongoDB usando variables de entorno
    connect(
        db=os.getenv("MONGODB_DB", "sgg_db"),
        host=os.getenv("MONGODB_URI", "mongodb://localhost:27017/sgg_db"),
        alias="default"
    )

    # Habilitar CORS
    CORS(app, supports_credentials=True)

    # Registrar Blueprints
    app.register_blueprint(instructor_bp, url_prefix="/api/instructores")
    app.register_blueprint(programa_bp, url_prefix="/api/programas")
    app.register_blueprint(guia_bp, url_prefix="/api/guias")

    return app
