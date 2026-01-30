from flask import Blueprint, request, jsonify
from app.repositories.instructor import InstructorRepository
from app.utils.security import generate_token, token_required

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"mensaje": "Usuario y contraseña son requeridos"}), 400

    username = data.get("username")
    password = data.get("password")
    
    instructor = InstructorRepository.obtener_por_username(username)
    
    if instructor and instructor.password == password:
        token = generate_token(instructor.id)
        return jsonify({
            "token": token,
            "instructor": instructor.to_dict()
        }), 200
    else:
        return jsonify({"mensaje": "Usuario o contraseña incorrectos"}), 401

@auth_bp.route("/me", methods=["GET"])
@token_required
def me(current_user):
    return jsonify(current_user.to_dict()), 200

@auth_bp.route("/logout", methods=["POST"])
def logout():
    # En JWT el logout se maneja en el cliente eliminando el token.
    # Pero podemos retornar éxito.
    return jsonify({"mensaje": "Sesión cerrada exitosamente"}), 200

