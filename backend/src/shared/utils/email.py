# app/utils/email.py
import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

yag = yagmail.SMTP(user=EMAIL_USER, password=EMAIL_PASSWORD)

def enviar_credenciales(email, username, password, full_name="Usuario"):
    asunto = f"Bienvenido a Saggi, {full_name} - Tus Credenciales"
    
    # HTML Template for a modern look
    cuerpo_html = f"""
    <html>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #333; line-height: 1.6;">
        <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #f9f9f9;">
            <div style="text-align: center; padding-bottom: 20px;">
                <h1 style="color: #4A90E2; margin: 0;">Saggi Grid Engine</h1>
                <p style="font-style: italic; color: #777;">"One Brain, Two Faces"</p>
            </div>
            
            <div style="background-color: #ffffff; padding: 25px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <h2 style="color: #333; margin-top: 0;">¡Hola, {full_name}!</h2>
                <p>Bienvenido(a) al ecosistema <strong>SGG (Saggi Grid Governance)</strong>. Estamos emocionados de tenerte a bordo.</p>
                
                <p>Se ha creado una cuenta para ti. Aquí tienes tus datos de acceso:</p>
                
                <div style="background-color: #f0f7ff; padding: 15px; border-left: 4px solid #4A90E2; margin: 20px 0;">
                    <p style="margin: 5px 0;"><strong>Usuario:</strong> <code style="background: #e1ecf4; padding: 2px 4px; border-radius: 3px;">{username}</code></p>
                    <p style="margin: 5px 0;"><strong>Contraseña:</strong> <code style="background: #e1ecf4; padding: 2px 4px; border-radius: 3px;">{password}</code></p>
                </div>
                
                <p style="font-size: 0.9em; color: #666;">
                    <em>Sugerencia: Por seguridad, te recomendamos cambiar tu contraseña en tu primer inicio de sesión.</em>
                </p>
                
                <div style="text-align: center; margin-top: 30px;">
                    <a href="#" style="background-color: #4A90E2; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold;">Acceder al Sistema</a>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 20px; font-size: 0.8em; color: #999;">
                <p>&copy; 2026 Equipo SGG. Todos los derechos reservados.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    try:
        yag.send(to=email, subject=asunto, contents=cuerpo_html)
        print(f"✅ Email personalizado enviado con éxito a {email}")
    except Exception as e:
        print(f"❌ Error al enviar email a {email}: {str(e)}")
        print(f"⚠️  Credenciales que fallaron:")
        print(f"   Usuario: {username}")
        print(f"   Password: {password}")
        # No re-lanzamos la excepción para que el registro del instructor no falle

