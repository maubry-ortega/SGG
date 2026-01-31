# SGG — Smart Guide Grid (Saggi)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Neon](https://img.shields.io/badge/Neon-PostgreSQL-31L8CE?style=for-the-badge&logo=postgresql)](https://neon.tech/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb)](https://www.mongodb.com/)

**SGG (Smart Guide Grid)** es un motor backend modular de alto rendimiento diseñado para gobernar procesos administrativos y de aprendizaje. La plataforma expuesta a la comunidad se conoce como **Saggi**.

> "Construye conocimiento con sistema, no con caos."

## 🐙 Pulpo Ingeniero SGG
La mascota representa inteligencia multitarea, coordinación distribuida y ejecución paralela. Un solo cerebro (SGG Core), muchos brazos (Servicios Modulares).

## 🚀 Características Clave
- **Un Cerebro, Dos Caras**: Branding dinámico para Comunidad (Saggi) vs Corporativo (SGG).
- **Persistencia Híbrida**: Neon PostgreSQL (Gobernanza) + MongoDB Atlas (Grid de Recursos de Aprendizaje).
- **RBAC y Seguridad**: Tokens JWT de Acceso/Refresco con control de acceso estricto basado en roles.
- **FastAPI Core**: Nativo asíncrono, tipado seguro y auto-documentado.

## 📁 Estructura del Repositorio
```
src/
├── api/v1/         # Endpoints versionados
├── core/           # Configuración, BD, lógica de seguridad
├── modules/        # Lógica de dominio (Auth, Learning, Gov, Branding)
├── shared/         # Modelos, utilidades y esquemas
└── main.py         # Punto de entrada
```

## 🛠️ Configuración y Ejecución

### 1. Requisitos
- Python 3.13+
- Archivo `.env` con credenciales de Neon y MongoDB.

### 2. Instalación
```bash
./venv/bin/pip install -r requirements.txt
```

### 3. Ejecutar Servidor de Desarrollo
```bash
./venv/bin/python3 -m uvicorn src.main:app --reload
```
El servidor iniciará en `http://localhost:8000`.

## 🧪 Pruebas
El sistema utiliza `pytest` con aislamiento de entorno.
```bash
./venv/bin/python3 -m pytest -v
```
*Nota: Las pruebas limpian automáticamente las tablas de prueba en Neon y MongoDB.*

## ⚛️ Integración con React
SGG está diseñado para ser consumido fácilmente por clientes modernos como React.

### Configuración CORS
La API ya está configurada para aceptar peticiones de cualquier origen en desarrollo (`allow_origins=["*"]`).

### Ejemplo de Consumo (Hooks)
```javascript
// Auth: Login y obtención de tokens
const login = async (username, password) => {
  const response = await fetch('http://localhost:8000/api/v1/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  const data = await response.json();
  // Guardar data.access_token y data.refresh_token
};

// Learning: Obtener recursos (Grid)
const getResources = async (token) => {
  const response = await fetch('http://localhost:8000/api/v1/learning/', {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return await response.json();
};
```

---
**SGG Core Engine - Modular, Escalable, Inteligente.**
