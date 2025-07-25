# VolleyDevByMaubry [2/∞]
# Cada módulo debe hacer bien una cosa y nada más.
from mongoengine import Document, StringField

class ProgramaFormacion(Document):
    name = StringField(required=True, unique=True)

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name
        }
