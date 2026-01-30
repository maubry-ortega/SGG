from flask import Blueprint, request, jsonify
from app.services.region import RegionService
from app.utils.security import token_required

region_bp = Blueprint("regiones_bp", __name__,url_prefix="/api/regiones")

@region_bp.route("/", methods=["GET"])
def listar_regiones():
    regiones = RegionService.listar_regiones()
    return jsonify([region.to_dict() for region in regiones]), 200

@region_bp.route("/", methods=["POST"])
@token_required
def crear_region(current_user):
    try:
        data = request.get_json()

        nombre = data.get("name")
        if not nombre:
            return jsonify({"error": "El nombre de la región es obligatorio."}), 400
        region = RegionService.crear_region(nombre)
        return jsonify(region.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        return jsonify({"error": "Error interno del servidor."}), 500
