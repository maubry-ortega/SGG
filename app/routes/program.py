from flask import Blueprint, request, jsonify
from app.services.program import ProgramaService

programa_bp = Blueprint('programa_bp', __name__, url_prefix='/api/programas')

@programa_bp.route('/', methods=['POST'])
def crear_programa():
    data = request.get_json()
    programa = ProgramaService.crear_programa(data)
    return jsonify(programa.to_dict()), 201

@programa_bp.route('/', methods=['GET'])
def listar_programas():
    programas = ProgramaService.listar_programas()
    return jsonify([p.to_dict() for p in programas]), 200

@programa_bp.route('/<string:id_>', methods=['GET'])
def obtener_programa(id_):
    try:
        programa = ProgramaService.obtener_programa(id_)
        return jsonify(programa.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@programa_bp.route('/<string:id_>', methods=['PUT'])
def actualizar_programa(id_):
    data = request.get_json()
    programa = ProgramaService.actualizar_programa(id_, data)
    return jsonify(programa.to_dict()), 200

@programa_bp.route('/<string:id_>', methods=['DELETE'])
def eliminar_programa(id_):
    ProgramaService.eliminar_programa(id_)
    return jsonify({'mensaje': 'Programa eliminado correctamente'}), 200
