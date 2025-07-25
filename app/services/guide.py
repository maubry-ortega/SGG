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
            filename = pdf_file.filename
            pdf_path = os.path.join(uploads_dir, filename)
            pdf_file.save(pdf_path)
            return filename
        return None

    @staticmethod
    def validarDatos(data, archivo):
        if not archivo or not hasattr(archivo, 'filename') or archivo.filename == '':
            return {"error": "No se anexó ningún PDF."}
        if not data.get('nombre'):
            return {"error": "El nombre es obligatorio."}
        if not data.get('descripcion'):
            return {"error": "La descripción es obligatoria."}
        if not data.get('programa'):
            return {"error": "El programa es obligatorio."}
        return True

    @staticmethod
    def dict_Guide(data):
        fecha_str = data.get("fecha")
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d') if fecha_str else datetime.now()

        instructor_id = session.get("instructor_id")
        if not instructor_id:
            raise ValueError("Instructor no autenticado.")

        instructor = Instructor.objects.get(id=instructor_id)
        programa = ProgramaFormacion.objects.get(id=data.get("programa"))

        return {
            "full_name": data.get("nombre"),
            "description": data.get("descripcion"),
            "date": fecha,
            "program": programa,
            "pdf_file": f'app/uploads/{data.get("archivo")}',
            "instructor": instructor
        }
