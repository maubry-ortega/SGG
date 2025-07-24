from flask_mail import Message
from flask import current_app
from app import mail

def enviar_credenciales(email, username, password):
    asunto = "Tus credenciales de acceso al sistema"
    cuerpo = f"""
    Hola,

    Bienvenido(a) al sistema SGG.

    Tus datos de acceso son:

    Usuario: {username}
    Contraseña: {password}

    Recuerda cambiar tu contraseña después de ingresar.

    Saludos,
    Equipo SGG
    """

    mensaje = Message(
        subject=asunto,
        recipients=[email],
        body=cuerpo
    )

    mail.send(mensaje)
