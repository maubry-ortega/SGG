from app.models.program import ProgramaFormacion
from mongoengine.errors import NotUniqueError, DoesNotExist
class ProgramaRepository:

    @staticmethod
    def crear(data):
        if not data.get('name'):
            raise ValueError("El campo 'name' es obligatorio.")
        
        programa = ProgramaFormacion(name=data['name'])
        try:
            programa.save()
            return programa
        except NotUniqueError:
            raise ValueError(f"El programa con el nombre '{data['name']}' ya existe.")

    @staticmethod
    def obtener_todos():
        return ProgramaFormacion.objects()

    @staticmethod
    def obtener_por_id(id_):
        try:
            return ProgramaFormacion.objects.get(id=id_)
        except (DoesNotExist, Exception):
            return None

    @staticmethod
    def actualizar(id_, data):
        if not data.get('name'):
            raise ValueError("El campo 'name' es obligatorio para actualizar.")
        
        programa = ProgramaFormacion.objects(id=id_).first()
        if not programa:
            return None
        
        programa.name = data['name']
        programa.save()
        return programa

    @staticmethod
    def eliminar(id_):
        programa = ProgramaFormacion.objects(id=id_).first()
        if not programa:
            return False
        programa.delete()
        return True

