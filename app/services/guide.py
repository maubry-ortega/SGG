import os
from flask import session
from datetime import datetime
from app.repositories.guide import GuiaRepository
from app.models.instructor import Instructor
from app.models.program import ProgramaFormacion

class GuiaService:

    @staticmethod
    def crear_guia(data):
        return GuiaRepository.crear(data)

    @staticmethod
    def listar_guias():
        return GuiaRepository.obtener_todos()

    @staticmethod
    def obtener_guia(id_):
        guia = GuiaRepository.obtener_por_id(id_)
        if not guia:
            raise ValueError("Guía no encontrada.")
        return guia

    @staticmethod
    def listar_guias_por_programa(id_programa):
        return GuiaRepository.obtener_por_programa(id_programa)

    @staticmethod
    def actualizar_guia(id_, data):
        return GuiaRepository.actualizar(id_, data)

    @staticmethod
    def eliminar_guia(id_):
        return GuiaRepository.eliminar(id_)

    @staticmethod
    def guardar_pdf(pdf_file):
        if pdf_file and hasattr(pdf_file, 'filename'):
            uploads_dir = 'app/uploads'
            os.makedirs(uploads_dir, exist_ok=True) 
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{pdf_file.filename}"
            pdf_path = os.path.join(uploads_dir, filename)
            pdf_file.save(pdf_path)
            return filename
        return None

    @staticmethod
    def validarDatos(data, archivo):
        if not archivo or not hasattr(archivo, 'filename') or archivo.filename == '':
            return {"error": "No se anexó ningún PDF."}
        if not data.get('full_name'):
            return {"error": "El nombre (full_name) es obligatorio."}
        if not data.get('description'):
            return {"error": "La descripción (description) es obligatoria."}
        if not data.get('program'):
            return {"error": "El programa (program) es obligatorio."}
        return True

    @staticmethod
    def dict_Guide(data, instructor):
        fecha_str = data.get("date") # Cambiado de fecha a date
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d') if fecha_str else datetime.now()

        programa = ProgramaFormacion.objects.get(id=data.get("program"))

        return {
            "full_name": data.get("full_name"),
            "description": data.get("description"),
            "date": fecha,
            "program": programa,
            "pdf_file": f'app/uploads/{data.get("archivo")}',
            "instructor": instructor
        }

