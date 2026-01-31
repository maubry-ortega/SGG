from typing import Dict, Any
from src.shared.models.user import UserIdentity

class BrandingService:
    @staticmethod
    def get_config(identity: UserIdentity) -> Dict[str, Any]:
        """Returns branding configuration based on User Identity."""
        if identity == UserIdentity.CORPORATE:
            return {
                "name": "SGG — Smart Guide Grid",
                "identity": "Corporate Architecture",
                "primary_color": "#1A202C",
                "mascot": "Pulpo Ingeniero SGG (Architect Mode)",
                "slogan": "Arquitectura y control para el conocimiento corporativo."
            }
        
        return {
            "name": "Saggi",
            "identity": "Community Learning Platform",
            "primary_color": "#3182CE",
            "mascot": "Pulpo Ingeniero Saggi (Guide Mode)",
            "slogan": "Saggi: Aprende estructurado. Avanza más rápido."
        }

    @staticmethod
    def get_mascot_message(action: str) -> str:
        """Pulpo Ingeniero messages based on user actions."""
        messages = {
            "login": "¡Bienvenido a la Grid! Mis ocho brazos están listos para organizar tu aprendizaje.",
            "create": "Nueva celda de conocimiento añadida a la Grid. ¡Excelente ejecución!",
            "error": "Parece que una conexión se soltó. Déjame reajustar los circuitos de la Grid."
        }
        return messages.get(action, "Manteniendo el sistema en orden.")
