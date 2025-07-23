# VolleyDevByMaubry [3/∞]
# El código que enseña también debe aprender de quien lo usa.
from mongoengine import Document, StringField, DateTimeField, ReferenceField, FileField
from datetime import datetime
from .instructor import Instructor
from .program import ProgramaFormacion

class GuiaAprendizaje(Document):
    nombre = StringField(required=True)
    descripcion = StringField()
    programa = ReferenceField(ProgramaFormacion, required=True)
    archivo_pdf = StringField(required=True)
    fecha = DateTimeField(default=datetime.utcnow)
    instructor = ReferenceField(Instructor, required=True)

    def to_dict(self):
        return {
            "id": str(self.id),
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "archivo_pdf": self.archivo_pdf,
            "fecha": self.fecha.isoformat(),
            "programa": self.programa.to_dict() if self.programa else None,
            "instructor": self.instructor.to_dict() if self.instructor else None
        }
