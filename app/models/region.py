from mongoengine import Document, StringField

class Region(Document):
    name = StringField(required=True, unique=True)

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name
        }
