from flask import Blueprint, request, jsonify
from app.services.guide import GuiaService
from app.utils.security import token_required

guia_bp = Blueprint('guia_bp', __name__, url_prefix='/api/guias')

@guia_bp.route('/', methods=['POST'])
@token_required
def crear_guia(current_user):
    try:
        # En una API, el frontend enviará FormData si hay archivos
        form_data = request.form.to_dict()
        archivo = request.files.get('archivo')

        validacion = GuiaService.validarDatos(form_data, archivo)
        if validacion is not True:
            return jsonify(validacion), 400

        nombre_pdf = GuiaService.guardar_pdf(archivo)
        form_data['archivo'] = nombre_pdf

        # Pasamos el current_user (instructor) al servicio
        dict_guide = GuiaService.dict_Guide(form_data, current_user)
        guia = GuiaService.crear_guia(dict_guide)

        return jsonify(guia.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500




@guia_bp.route('/', methods=['GET'])
def listar_guias():
    guias = GuiaService.listar_guias()
    return jsonify([g.to_dict() for g in guias]), 200

@guia_bp.route('/buscar/<string:id_>', methods=['GET'])
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
@token_required
def actualizar_guia(current_user, id_):
    try:
        data = request.get_json()
        guia = GuiaService.actualizar_guia(id_, data)
        return jsonify(guia.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@guia_bp.route('/<string:id_>', methods=['DELETE'])
@token_required
def eliminar_guia(current_user, id_):
    try:
        GuiaService.eliminar_guia(id_)
        return jsonify({'mensaje': 'Guía eliminada correctamente'}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
