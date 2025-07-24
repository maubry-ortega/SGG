# VolleyDevByMaubry [11/∞]
from app.models.region import Region
from mongoengine.errors import DoesNotExist

class RegionRepository:

    @staticmethod
    def obtener_todas():
        return Region.objects()

    @staticmethod
    def obtener_por_id(id):
        try:
            return Region.objects.get(id=id)
        except DoesNotExist:
            return None

    @staticmethod
    def crear(nombre):
        region = Region(name=nombre)
        region.save()
        return region
