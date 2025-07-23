# VolleyDevByMaubry [3/∞]
# El código que enseña también debe aprender de quien lo usa.
from mongoengine import Document, StringField, DateTimeField, ReferenceField, FileField
from datetime import datetime
from .instructor import Instructor
from .programa import ProgramaFormacion

class GuiaAprendizaje(Document):
    meta = {"collection": "guias_aprendizaje"}

    nombre = StringField(required=True)
    descripcion = StringField()
    programa = ReferenceField(ProgramaFormacion, required=True)
    archivo_pdf = StringField(required=True)  # Ruta al archivo en /uploads
    fecha = DateTimeField(default=datetime.utcnow)
    instructor = ReferenceField(Instructor, required=True)

    def to_dict(self):
        return {
            "id": str(self.id),
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "programa": self.programa.nombre if self.programa else None,
            "archivo_pdf": self.archivo_pdf,
            "fecha": self.fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "instructor": self.instructor.nombre_completo if self.instructor else None,
            "regional": self.instructor.regional if self.instructor else None,
        }
