from flask import Blueprint, request, jsonify
from app.services.program import ProgramaService

programa_bp = Blueprint('programa_bp', __name__, url_prefix='/api/programas')

@programa_bp.route('/', methods=['POST'])
def crear_programa():
    data = request.get_json()
    programa = ProgramaService.crear_programa(data)
    if programa is None:
        return jsonify({'error': 'Datos inválidos para crear el programa...'}), 400
    else:
        return programa

@programa_bp.route('/', methods=['GET'])
def listar_programas():
    print("Listando programas...")
    programas = ProgramaService.listar_programas()
    return jsonify([p.to_dict() for p in programas]), 200

@programa_bp.route('/<string:id_>', methods=['GET'])
def obtener_programa(id_):
    programa = ProgramaService.obtener_programa(id_)
    return (programa), 200


@programa_bp.route('/<string:id_>', methods=['PUT'])
def actualizar_programa(id_):
    data = request.get_json()
    programa = ProgramaService.actualizar_programa(id_, data)
    return programa, 200

@programa_bp.route('/<string:id_>', methods=['DELETE'])
def eliminar_programa(id_):
    return ProgramaService.eliminar_programa(id_), 200
