from flask import Blueprint, request, jsonify
from app.services.program import ProgramaService
from app.utils.security import token_required

programa_bp = Blueprint('programa_bp', __name__, url_prefix='/api/programas')

@programa_bp.route('/', methods=['POST'])
@token_required
def crear_programa(current_user):
    try:
        data = request.get_json()
        programa = ProgramaService.crear_programa(data)
        return jsonify(programa.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@programa_bp.route('/', methods=['GET'])
def listar_programas():
    try:
        programas = ProgramaService.listar_programas()
        return jsonify([p.to_dict() for p in programas]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@programa_bp.route('/<string:id_>', methods=['GET'])
def obtener_programa(id_):
    try:
        programa = ProgramaService.obtener_programa(id_)
        if not programa:
            return jsonify({'error': 'Programa no encontrado'}), 404
        return jsonify(programa.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@programa_bp.route('/<string:id_>', methods=['PUT'])
@token_required
def actualizar_programa(current_user, id_):
    try:
        data = request.get_json()
        programa = ProgramaService.actualizar_programa(id_, data)
        if not programa:
            return jsonify({'error': 'No se pudo actualizar el programa'}), 400
        return jsonify(programa.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@programa_bp.route('/<string:id_>', methods=['DELETE'])
@token_required
def eliminar_programa(current_user, id_):
    try:
        mensaje = ProgramaService.eliminar_programa(id_)
        return jsonify({'mensaje': mensaje or 'Programa eliminado'}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
