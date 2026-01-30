import jwt
import datetime
import os
from functools import wraps
from flask import request, jsonify
from app.models.instructor import Instructor

SECRET_KEY = os.getenv("SECRET_KEY", "clave-super-secreta")

def generate_token(instructor_id):
    """Genera un token JWT para un instructor"""
    try:
        now = datetime.datetime.now(datetime.UTC)
        payload = {
            'exp': now + datetime.timedelta(days=1),
            'iat': now,
            'sub': str(instructor_id)
        }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )

    except Exception as e:
        return str(e)

def token_required(f):
    """Decorador para proteger rutas con JWT"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({'message': 'Token faltante'}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = Instructor.objects.get(id=data['sub'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'El token ha expirado'}), 401
        except (jwt.InvalidTokenError, Exception):
            return jsonify({'message': 'Token inválido'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
