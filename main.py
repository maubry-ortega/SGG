import threading
import justpy as jp
from app import create_app

# Crear instancia de la app Flask
flask_app = create_app()

# Ruta simple para probar que Flask funciona
@flask_app.route("/api/ping")
def ping():
    return {"message": "pong"}

# Interfaz visual con JustPy
def gui_frontend():
    wp = jp.QuasarPage()
    jp.QDiv(a=wp, text="Sistema Gestor de Guías (SGG)", classes="text-h3 text-center q-mt-xl")
    return wp

# Lanzar JustPy en hilo paralelo para no bloquear Flask
def run_justpy():
    jp.justpy(gui_frontend, port=8080)

# Main principal
if __name__ == "__main__":
    # Iniciar JustPy en segundo plano
    threading.Thread(target=run_justpy, daemon=True).start()

    # Ejecutar Flask normalmente
    flask_app.run(debug=True, port=5000)
