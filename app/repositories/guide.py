from app.models.guide import GuiaAprendizaje

class GuiaRepository:

    @staticmethod
    def crear(data):
        try:
            guia = GuiaAprendizaje(**data)
            guia.save()
            return guia
        except Exception as error:
            raise ValueError(f"Error al crear la guía: {str(error)}")

    @staticmethod
    def obtener_todos():
        return GuiaAprendizaje.objects()

    @staticmethod
    def obtener_por_id(id_):
        return GuiaAprendizaje.objects(id=id_).first()

    @staticmethod
    def obtener_por_programa(id_programa):
        return GuiaAprendizaje.objects(program=id_programa) # Corregido field name 'program'

    @staticmethod
    def actualizar(id_, data):
        guia = GuiaAprendizaje.objects(id=id_).first()
        if not guia:
            return None
        
        for key, value in data.items():
            if hasattr(guia, key):
                setattr(guia, key, value)
        
        guia.save()
        return guia

    @staticmethod
    def eliminar(id_):
        guia = GuiaAprendizaje.objects(id=id_).first()
        if not guia:
            return False
        guia.delete()
        return True

