from app.repositories.program import ProgramaRepository

class ProgramaService:

    @staticmethod
    def crear_programa(data):
        if not data:
            return None
        else:
            return ProgramaRepository.crear(data)

    @staticmethod
    def listar_programas():
        return ProgramaRepository.obtener_todos()

    @staticmethod
    def obtener_programa(id_):
        programa = ProgramaRepository.obtener_por_id(id_)
        if not programa:
            raise ValueError("Programa no encontrado.")
        return programa

    @staticmethod
    def actualizar_programa(id_, data):
        return ProgramaRepository.actualizar(id_, data)

    @staticmethod
    def eliminar_programa(id_):
        return ProgramaRepository.eliminar(id_)
