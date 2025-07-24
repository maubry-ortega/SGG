from app.repositories.instructor import InstructorRepository

class InstructorService:

    @staticmethod
    def crear_instructor(data):
        if InstructorRepository.obtener_por_usuario(data.get("usuario")):
            raise ValueError("El usuario ya existe.")
        return InstructorRepository.crear(data)

    @staticmethod
    def listar_instructores():
        return InstructorRepository.obtener_todos()

    @staticmethod
    def obtener_instructor(uid):
        instructor = InstructorRepository.obtener_por_uid(uid)
        if not instructor:
            raise ValueError("Instructor no encontrado.")
        return instructor

    @staticmethod
    def actualizar_instructor(uid, data):
        return InstructorRepository.actualizar(uid, data)

    @staticmethod
    def eliminar_instructor(uid):
        return InstructorRepository.eliminar(uid)
