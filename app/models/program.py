# VolleyDevByMaubry [2/∞]
# Cada módulo debe hacer bien una cosa y nada más.
from mongoengine import Document, StringField

class ProgramaFormacion(Document):
    nombre = StringField(required=True, unique=True)
