from app.repositories.instructor import InstructorRepository
from app.models.region import Region
from mongoengine.errors import ValidationError, NotUniqueError
from app.utils.email import enviar_credenciales
import random
import string

class InstructorService:

    @staticmethod
    def _generar_password(longitud=10):
        caracteres = string.ascii_letters + string.digits + "!@#$%&*"
        return ''.join(random.choices(caracteres, k=longitud))

    @staticmethod
    def crear_instructor(data):
        print("holamundo")
        campos_requeridos = ["full_name", "email", "region", "username"]
        for campo in campos_requeridos:
            if not data.get(campo):
                raise ValueError(f"El campo '{campo}' es obligatorio.")

        if InstructorRepository.obtener_por_email(data["email"]):
            raise ValueError("Ya existe un instructor con este correo.")

        if InstructorRepository.obtener_por_username(data["username"]):
            raise ValueError("Ya existe un instructor con este nombre de usuario.")
        print("try para obtener regiones")
        try:
            region = Region.objects.get(id=data["region"])
            print("region obtenida con exito: " )
        except Region.DoesNotExist:
            raise ValueError("La región especificada no existe.")

        # 1. Usar contraseña proporcionada o generar una aleatoria
        password_generada = data.get("password") or InstructorService._generar_password()
        print("json de creacion")
        datos_creacion = {
            "full_name": data["full_name"],
            "email": data["email"],
            "region": region,
            "username": data["username"],
            "password": password_generada
        }

        print("try para crear instructor")
        try:
            # 3. Crear instructor en la base de datos
            instructor = InstructorRepository.crear(datos_creacion)
            print("instructor creado")
            # 4. Enviar credenciales al correo
            enviar_credenciales(
                email=data["email"],
                username=data["username"],
                password=password_generada
            )
            print("listo para retornar instructor")
            return instructor
        except (ValidationError, NotUniqueError) as e:
            print(f"error capturado:{str(e)}")
            raise ValueError(f"No se pudo crear el instructor: {str(e)}")

    @staticmethod
    def obtener_todos():
        return InstructorRepository.obtener_todos()

    @staticmethod
    def obtener_por_id(id):
        instructor = InstructorRepository.obtener_por_id(id)
        if not instructor:
            raise ValueError("Instructor no encontrado.")
        return instructor

    @staticmethod
    def actualizar_instructor(id, nuevos_datos):
        instructor = InstructorRepository.actualizar(id, nuevos_datos)
        if not instructor:
            raise ValueError("No se pudo actualizar el instructor.")
        return instructor

    @staticmethod
    def eliminar_instructor(id):
        eliminado = InstructorRepository.eliminar(id)
        if not eliminado:
            raise ValueError("Instructor no encontrado.")
