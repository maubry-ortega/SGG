from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.repositories.instructor import InstructorRepository
from app.repositories.program import ProgramaRepository

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def index():
    return redirect(url_for("auth.login"))

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        instructor = InstructorRepository.obtener_por_username(username)
        if instructor and instructor.password == password:
            session["instructor_id"] = str(instructor.id)
            return redirect(url_for("auth.menu"))
        else:
            flash("Usuario o contraseña incorrectos", "danger")
    return render_template("login.html")

@auth_bp.route("/registro")
def registro():
    return render_template("registro.html")

@auth_bp.route("/formulario-guia")
def formulario_guia():
    programas = ProgramaRepository.obtener_todos()
    return render_template("form_guide.html", programas=programas)

@auth_bp.route("/exito")
def exito():
    # Después del registro exitoso, mostrar el menú principal
    return render_template("menu.html")
# Ruta para el menú principal
@auth_bp.route("/menu")
def menu():
    # Solo mostrar si el usuario está autenticado
    if "instructor_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template("menu.html")

@auth_bp.route("/error")
def error():
    mensaje_error = request.args.get("msg", "Ha ocurrido un error.")
    return render_template("error.html", mensaje_error=mensaje_error)

# Ruta para cerrar sesión
@auth_bp.route("/logout")
def logout():
    session.pop("instructor_id", None)
    return redirect(url_for("auth.login"))
