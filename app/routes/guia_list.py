# app/routes/guia_list.py
from flask import Blueprint, render_template
from app.models.guide import GuiaAprendizaje
from app.models.instructor import Instructor
from app.models.program import ProgramaFormacion
from app.models.region import Region

# Blueprint para listar guías
lista_guias_bp = Blueprint('lista_guias', __name__)

@lista_guias_bp.route('/guias', methods=['GET'])
def listar_guias():
    guias = GuiaAprendizaje.objects.all()
    guias_data = []
    for guia in guias:
        instructor = Instructor.objects(id=guia.instructor_id).first()
        programa = ProgramaFormacion.objects(id=guia.programa_id).first()
        region = Region.objects(id=instructor.region_id).first() if instructor else None
        guias_data.append({
            'nombre': guia.nombre,
            'descripcion': guia.descripcion,
            'programa': programa.nombre if programa else '',
            'instructor': instructor.nombre if instructor else '',
            'regional': region.nombre if region else '',
            'fecha': guia.fecha_publicacion.strftime('%d/%m/%Y') if hasattr(guia, 'fecha_publicacion') else '',
            'pdf_url': guia.pdf_url if hasattr(guia, 'pdf_url') else ''
        })
    return render_template('guias.html', guias=guias_data)
