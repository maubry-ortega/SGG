from app.repositories.guide import GuiaRepository

class GuiaService:

    @staticmethod
    def crear_guia(data):
        return GuiaRepository.crear(data)

    @staticmethod
    def listar_guias():
        return GuiaRepository.obtener_todos()

    @staticmethod
    def obtener_guia(id_):
        guia = GuiaRepository.obtener_por_id(id_)
        if not guia:
            raise ValueError("Guía no encontrada.")
        return guia

    @staticmethod
    def listar_guias_por_programa(id_programa):
        return GuiaRepository.obtener_por_programa(id_programa)

    @staticmethod
    def actualizar_guia(id_, data):
        return GuiaRepository.actualizar(id_, data)

    @staticmethod
    def eliminar_guia(id_):
        return GuiaRepository.eliminar(id_)
