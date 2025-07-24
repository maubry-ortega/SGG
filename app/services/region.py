# VolleyDevByMaubry [12/∞]
from app.repositories.region import RegionRepository
from mongoengine.errors import NotUniqueError, ValidationError

class RegionService:

    @staticmethod
    def listar_regiones():
        return RegionRepository.obtener_todas()

    @staticmethod
    def crear_region(nombre):
        try:
            return RegionRepository.crear(nombre)
        except (ValidationError, NotUniqueError):
            raise ValueError("Ya existe una región con ese nombre.")
