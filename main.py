from app import create_app

# Crear instancia de la app Flask
flask_app = create_app()

# Ruta simple para probar que Flask funciona
@flask_app.route("/api/ping")
def ping():
    return {"message": "pong"}

# Main principal
if __name__ == "__main__":
    flask_app.run(debug=True, port=5000)
