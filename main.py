from flask import Flask
import justpy as jp

flask_app = Flask(__name__)

@flask_app.route("/api/guias")
def api_guias():
    return {"guias": ["Guía 1", "Guía 2"]}

def gui_frontend():
    wp = jp.QuasarPage()
    jp.QDiv(a=wp, text="Desde Flask + JustPy", classes="text-h5")
    return wp

# Levantar solo JustPy como app principal si no usas Flask puro
if __name__ == "__main__":
    jp.justpy(gui_frontend)
