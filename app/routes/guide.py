from flask import Blueprint, request, jsonify
from app.services.guide import GuiaService

guia_bp = Blueprint('guia_bp', __name__, url_prefix='/api/guias')

@guia_bp.route('/', methods=['POST'])
def crear_guia():
    data = request.get_json()
    guia = GuiaService.crear_guia(data)
    return jsonify(guia.to_dict()), 201

@guia_bp.route('/', methods=['GET'])
def listar_guias():
    guias = GuiaService.listar_guias()
    return jsonify([g.to_dict() for g in guias]), 200

@guia_bp.route('/<string:id_>', methods=['GET'])
def obtener_guia(id_):
    try:
        guia = GuiaService.obtener_guia(id_)
        return jsonify(guia.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@guia_bp.route('/programa/<string:id_programa>', methods=['GET'])
def listar_guias_por_programa(id_programa):
    guias = GuiaService.listar_guias_por_programa(id_programa)
    return jsonify([g.to_dict() for g in guias]), 200

@guia_bp.route('/<string:id_>', methods=['PUT'])
def actualizar_guia(id_):
    data = request.get_json()
    guia = GuiaService.actualizar_guia(id_, data)
    return jsonify(guia.to_dict()), 200

@guia_bp.route('/<string:id_>', methods=['DELETE'])
def eliminar_guia(id_):
    GuiaService.eliminar_guia(id_)
    return jsonify({'mensaje': 'Guía eliminada correctamente'}), 200
