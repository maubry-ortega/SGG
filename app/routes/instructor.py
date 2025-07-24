from flask import Blueprint, request, jsonify
from app.services.instructor import InstructorService

instructor_bp = Blueprint('instructor_bp', __name__, url_prefix='/api/instructores')

@instructor_bp.route('/', methods=['POST'])
def crear_instructor():
    data = request.get_json()
    try:
        instructor = InstructorService.crear_instructor(data)
        return jsonify(instructor.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@instructor_bp.route('/', methods=['GET'])
def listar_instructores():
    instructores = InstructorService.listar_instructores()
    return jsonify([i.to_dict() for i in instructores]), 200

@instructor_bp.route('/<string:uid>', methods=['GET'])
def obtener_instructor(uid):
    try:
        instructor = InstructorService.obtener_instructor(uid)
        return jsonify(instructor.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@instructor_bp.route('/<string:uid>', methods=['PUT'])
def actualizar_instructor(uid):
    data = request.get_json()
    instructor = InstructorService.actualizar_instructor(uid, data)
    return jsonify(instructor.to_dict()), 200

@instructor_bp.route('/<string:uid>', methods=['DELETE'])
def eliminar_instructor(uid):
    InstructorService.eliminar_instructor(uid)
    return jsonify({'mensaje': 'Instructor eliminado correctamente'}), 200
