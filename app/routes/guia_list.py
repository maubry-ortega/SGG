from flask import Blueprint, render_template
from app.services.guide import GuiaService

guide_list_bp = Blueprint("guide_list_bp", __name__, url_prefix="/guias")

@guide_list_bp.route("/", methods=["GET"])
def list_guides():
    try:
        guides = GuiaService.listar_guias()

        guide_data = []
        for guide in guides:
            guide_info = {
                "id": str(guide.id),
                "name": guide.full_name,
                "description": guide.description,
                "date": guide.date.strftime('%Y-%m-%d') if guide.date else "Sin fecha",
                "program_name": guide.program.name if guide.program else "Sin programa",
                "instructor_name": guide.instructor.full_name if guide.instructor else "Sin instructor",
                "pdf_file": guide.pdf_file
            }
            guide_data.append(guide_info)

        return render_template("guias.html", guides=guide_data)

    except Exception as e:
        return render_template("error.html", mensaje_error=f"Ocurrió un error al cargar las guías: {str(e)}")
