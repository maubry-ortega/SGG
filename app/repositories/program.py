from app.models.program import ProgramaFormacion

class ProgramaRepository:

    @staticmethod
    def crear(data):
        return ProgramaFormacion(**data).save()

    @staticmethod
    def obtener_todos():
        return ProgramaFormacion.objects()

    @staticmethod
    def obtener_por_id(id_):
        return ProgramaFormacion.objects(id=id_).first()

    @staticmethod
    def actualizar(id_, data):
        return ProgramaFormacion.objects(id=id_).update_one(**data)

    @staticmethod
    def eliminar(id_):
        return ProgramaFormacion.objects(id=id_).delete()
