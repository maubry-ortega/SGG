# VolleyDevByMaubry [8/∞]
from app.repositories.instructor import InstructorRepository
from app.models.region import Region
from mongoengine.errors import ValidationError, NotUniqueError
from app.utils.email import enviar_credenciales  # 👈 nuevo import

class InstructorService:

    @staticmethod
    def crear_instructor(data):
        campos_requeridos = ["full_name", "email", "region", "username", "password"]
        for campo in campos_requeridos:
            if not data.get(campo):
                raise ValueError(f"El campo '{campo}' es obligatorio.")

        if InstructorRepository.obtener_por_email(data["email"]):
            raise ValueError("Ya existe un instructor con este correo.")

        if InstructorRepository.obtener_por_username(data["username"]):
            raise ValueError("Ya existe un instructor con este nombre de usuario.")

        try:
            region = Region.objects.get(id=data["region"])
        except Region.DoesNotExist:
            raise ValueError("La región especificada no existe.")

        data["region"] = region

        try:
            instructor = InstructorRepository.crear(data)

            # ✅ Enviar correo con credenciales
            try:
                enviar_credenciales(
                    email=data["email"],
                    username=data["username"],
                    password=data["password"]
                )
            except Exception as e:
                print(f"[!] Error enviando correo a {data['email']}: {e}")

            return instructor
        except (ValidationError, NotUniqueError) as e:
            raise ValueError(f"No se pudo crear el instructor: {str(e)}")
