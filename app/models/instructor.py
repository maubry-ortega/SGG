# VolleyDevByMaubry [1/∞]
# El conocimiento solo florece cuando se comparte.
from mongoengine import Document, StringField
import uuid

class Instructor(Document):
    nombre_completo = StringField(required=True, max_length=120)
    correo = StringField(required=True, unique=True)
    regional = StringField(required=True, choices=["Cauca", "Huila", "Antioquia", "Valle", "Nariño"])
    usuario = StringField(required=True, unique=True)
    contraseña = StringField(required=True)

    def to_dict(self):
        return {
            "uid": str(self.id),
            "nombre_completo": self.nombre_completo,
            "correo": self.correo,
            "regional": self.regional,
            "usuario": self.usuario
            # Ojo: no devuelvas la contraseña en producción
        }
