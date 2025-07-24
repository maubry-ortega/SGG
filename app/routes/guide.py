from flask import Blueprint, request, jsonify,render_template
from app.services.guide import GuiaService
from app.services.program import ProgramaService
guia_bp = Blueprint('guia_bp', __name__, url_prefix='/api/guias')

@guia_bp.route('/Create', methods=['POST', 'GET'])
def crear_guia():
    try:
        if request.method == 'GET':   
            Programas = ProgramaService.listar_programas()
            return render_template('form_guide.html',programas=Programas)
        else:
            data = request.form
            guide_date
            if GuiaService.validarDatos(data):
                dict_guide = GuiaService.dict_Guide(data)
                guide= GuiaService.crear_guia(dict_guide)
                return jsonify(guide.to_dict())
            else:
                return jsonify({"error": "Datos inválidos"})
    except Exception as e:
        return jsonify({"error": str(e)})

    
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
def actualizar_guia(id_):
    data = request.get_json()
    guia = GuiaService.actualizar_guia(id_, data)
    return jsonify(guia.to_dict()), 200

@guia_bp.route('/<string:id_>', methods=['DELETE'])
def eliminar_guia(id_):
    GuiaService.eliminar_guia(id_)
    return jsonify({'mensaje': 'Guía eliminada correctamente'}), 200
