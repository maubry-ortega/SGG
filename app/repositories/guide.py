from app.models.guide import GuiaAprendizaje

class GuiaRepository:

    @staticmethod
    def crear(data):
        try:
            guia = GuiaAprendizaje(**data).save()
            return {"Guia": guia.to_dict()}
        except Exception as error:
            mensaje = f"Error inesperado al crear la guía: {str(error)}"
            return {"Error": mensaje}
            
    

    @staticmethod
    def obtener_todos():
        return GuiaAprendizaje.objects()

    @staticmethod
    def obtener_por_id(id_):
        return GuiaAprendizaje.objects(id=id_).first()

    @staticmethod
    def obtener_por_programa(id_programa):
        return GuiaAprendizaje.objects(programa=id_programa)

    @staticmethod
    def actualizar(id_, data):
        return GuiaAprendizaje.objects(id=id_).update_one(**data)

    @staticmethod
    def eliminar(id_):
        return GuiaAprendizaje.objects(id=id_).delete()
