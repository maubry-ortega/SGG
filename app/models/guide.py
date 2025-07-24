# VolleyDevByMaubry [3/∞]
# El código que enseña también debe aprender de quien lo usa.
from mongoengine import Document, StringField, DateTimeField, ReferenceField, FileField
from datetime import datetime
from .instructor import Instructor
from .program import ProgramaFormacion

class GuiaAprendizaje(Document):
    full_name = StringField(required=True)
    description = StringField()
    program = ReferenceField(ProgramaFormacion, required=True)
    pdf_file = StringField(required=True)
    date = DateTimeField(default=datetime.utcnow)
    instructor = ReferenceField(Instructor, required=True)

    def to_dict(self):
        return {
            "id": str(self.id),
            "full_name": self.full_name,
            "description": self.description,
            "pdf_file": self.pdf_file,
            "date": self.date.isoformat(),
            "program": self.program.to_dict() if self.program else None,
            "instructor": self.instructor.to_dict() if self.instructor else None
        }
