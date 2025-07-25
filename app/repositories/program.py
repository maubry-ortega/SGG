from app.models.program import ProgramaFormacion
from mongoengine.errors import NotUniqueError, DoesNotExist
class ProgramaRepository:

    @staticmethod
    def crear(data):
        try:
            if data['name'] == '' or data['name'] is None:
                return {"Error": "El campo 'name'no puede ser vacio y es obligatorio para crear un programa."}
            else:
                programa=ProgramaFormacion(**data).save()
                return {"programa": programa.to_dict()}
        except NotUniqueError as error:
            mensaje= f"El name del programa ya existe!...Error:  {str(error)}"
            return {"Error":mensaje}
        except Exception as error:
            mensaje = f"Error inesperado al crear el programa: {str(error)}"
            return {"Error":mensaje}
    


    @staticmethod
    def obtener_todos():
        try:
            return ProgramaFormacion.objects()
        except Exception as error:
            mensaje = f"Error inesperado al obtener programas: {str(error)}"
            return {"mensaje":mensaje}


    @staticmethod
    def obtener_por_id(id_):
        try:
            programa=ProgramaFormacion.objects(id=id_).first()
            if len(programa) > 0:
                return programa.to_dict()
            else:
                return {"mensaje": f"No existe un programa con el ID {id_}"}
        except DoesNotExist:
            mensaje = f"Error de con el ID {id_}: {str(error)}"
            return {"mensaje": mensaje}
        except Exception as error:
            mensaje = f"Error inesperado con ID {id_}: {str(error)}"
            return {"mensaje":mensaje}

    @staticmethod
    def actualizar(id_, data):
        try:
            if data['name'] == '' or data['name'] is None:
                return {"Error": "El campo 'name' no puede ser vacio y es obligatorio para actualizar un programa."}
            else:
                ProgramaFormacion.objects(id=id_).update_one(**data)
                programa = ProgramaFormacion.objects(id=id_).first()
                return {"programa Actualizado": programa.to_dict()}
        except DoesNotExist as error:
            mensaje = f"Programa con ID {id_} no existe: {str(error)}"
            return {"Error": mensaje}
        except Exception as error:
            mensaje = f"Error inesperado al actualizar el programa: {str(error)}"
            return {"Error": mensaje}

    @staticmethod
    def eliminar(id_):
        try:
            programa = ProgramaFormacion.objects(id=id_).first()
            ProgramaFormacion.objects(id=id_).delete()
            return {"Pelicula Eliminada": programa.to_dict()}
        except DoesNotExist as error:
            mensaje = f"Programa con ID {id_} no existe: {str(error)}"
            return {"Error": mensaje}
        except Exception as error:
            mensaje = f"Error inesperado al eliminar el programa: {str(error)}"
            return {"Error": mensaje}
