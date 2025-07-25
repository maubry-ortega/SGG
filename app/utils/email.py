# app/utils/email.py
import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

yag = yagmail.SMTP(user=EMAIL_USER, password=EMAIL_PASSWORD)

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
    yag.send(to=email, subject=asunto, contents=cuerpo)
