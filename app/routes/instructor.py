# VolleyDevByMaubry [9/∞]
from flask import Blueprint, request, jsonify
from app.services.instructor import InstructorService

instructor_bp = Blueprint("instructor", __name__, url_prefix="/api/instructores")

@instructor_bp.route("/", methods=["POST"])
def crear_instructor():
    try:
        data = request.get_json()
        instructor = InstructorService.crear_instructor(data)
        return jsonify(instructor.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500

@instructor_bp.route("/", methods=["GET"])
def listar_instructores():
    instructores = InstructorService.()
    return jsonify([i.to_dict() for i in instructores]), 200

@instructor_bp.route("/<string:id>", methods=["GET"])
def obtener_instructor(id):
    try:
        instructor = InstructorService.obtener_por_id(id)
        return jsonify(instructor.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@instructor_bp.route("/<string:id>", methods=["PUT"])
def actualizar_instructor(id):
    try:
        nuevos_datos = request.get_json()
        instructor = InstructorService.actualizar_instructor(id, nuevos_datos)
        return jsonify(instructor.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@instructor_bp.route("/<string:id>", methods=["DELETE"])
def eliminar_instructor(id):
    try:
        InstructorService.eliminar_instructor(id)
        return jsonify({"mensaje": "Instructor eliminado exitosamente."}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
