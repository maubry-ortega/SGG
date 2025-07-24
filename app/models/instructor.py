# VolleyDevByMaubry [6/∞]
# El conocimiento solo florece cuando se comparte.
from mongoengine import Document, StringField, ReferenceField
from .region import Region

class Instructor(Document):
    full_name = StringField(required=True, max_length=120)
    email = StringField(required=True, unique=True)
    region = ReferenceField(Region, required=True)
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

    def to_dict(self):
        return {
            "id": str(self.id),
            "full_name": self.full_name,
            "email": self.email,
            "region": self.region.name if self.region else None,
            "username": self.username
            # No incluimos password por seguridad
        }
