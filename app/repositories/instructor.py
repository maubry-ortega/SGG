# VolleyDevByMaubry [4/∞]
# La base de los datos es el silencio bien estructurado.
from app.models.instructor import Instructor

class InstructorRepository:

    @staticmethod
    def crear(data):
        return Instructor(**data).save()

    @staticmethod
    def obtener_todos():
        return Instructor.objects()

    @staticmethod
    def obtener_por_uid(uid):
        return Instructor.objects(uid=uid).first()

    @staticmethod
    def obtener_por_usuario(usuario):
        return Instructor.objects(usuario=usuario).first()

    @staticmethod
    def actualizar(uid, data):
        return Instructor.objects(uid=uid).update_one(**data)

    @staticmethod
    def eliminar(uid):
        return Instructor.objects(uid=uid).delete()
