from app.repositories.guide import GuiaRepository

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
        
        if pdf_file:
            pdf_path = f'app/uploads/{pdf_file.filename}'
            pdf_file.save(pdf_path)
            ##data = data.to_dict()
            ##data['pdf_path'] = pdf_path
        else:
            return None
        return True
        
    @staticmethod
    def validarDatos(data):
        if  GuiaService.guardar_pdf(data.get('archivo')):
            return {"error":"No se guardó...No se anexó ningun PDF..."}
        if not data.get('nombre'):
            return {"error":"El nombre es obligatorio."}
        if not data.get('descripcion'):
            return {"error":"La descripción es obligatoria."}
        if not data.get('fecha'):
            return {"error":"La fecha es obligatoria."}
        if not data.get('programa'):
            return {"error":"El programa es obligatorio."}
        
    def dict_Guide(data):
        return {
            "nombre": data.get("nombre"),
            "descripcion": data.get("descripcion"),
            "fecha": data.get("fecha"),
            "programa": data.get("programa"),
            "pdf_path": f'app/uploads/{data["archivo"].filename}'
        }