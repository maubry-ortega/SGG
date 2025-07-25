from app.models.instructor import Instructor
from bson import ObjectId
from mongoengine.errors import DoesNotExist, ValidationError

class InstructorRepository:

    @staticmethod
    def crear(data):
        instructor = Instructor(**data)
        instructor.save()
        return instructor.to_dict()

    @staticmethod
    def obtener_todos():
        return Instructor.objects()

    @staticmethod
    def obtener_por_id(id):
        try:
            return Instructor.objects.get(id=ObjectId(id))
        except (DoesNotExist, Exception):
            return None

    @staticmethod
    def obtener_por_username(username):
        return Instructor.objects(username=username).first()

    @staticmethod
    def obtener_por_email(email):
        return Instructor.objects(email=email).first()

    @staticmethod
    def actualizar(id, nuevos_datos):
        instructor = InstructorRepository.obtener_por_id(id)
        if not instructor:
            return None

        for campo, valor in nuevos_datos.items():
            if hasattr(instructor, campo):
                setattr(instructor, campo, valor)

        try:
            instructor.save()
        except ValidationError:
            return None

        return instructor

    @staticmethod
    def eliminar(id):
        instructor = InstructorRepository.obtener_por_id(id)
        if instructor:
            instructor.delete()
            return True
        return False
