# SGG - Sistema Gestor de Guías (API REST)

SGG (Sistema Gestor de Guías) ha sido transformado en una **API REST pura** diseñada para ser consumida por frontends modernos (como React). Este sistema permite la gestión eficiente de guías de aprendizaje, instructores, programas de formación y regiones de manera segura y escalable.

## Características principales

- **API RESTful Pura**: Todas las respuestas son en formato JSON estándar.
- **Autenticación JWT**: Seguridad sin estado mediante JSON Web Tokens para proteger los recursos.
- **Gestión de Guías**: Registro (con carga de PDF), listado, búsqueda, actualización y eliminación.
- **Gestión de Instructores**: Registro con validaciones, generación de contraseñas y envío de credenciales por email.
- **Gestión de Recursos**: CRUD completo para Programas de Formación y Regiones.
- **CORS Habilitado**: Configurado para permitir peticiones desde entornos de desarrollo frontend (localhost:3000).
- **Suite de Pruebas**: Cobertura automatizada con Pytest para asegurar la integridad de la API.

## Estructura del proyecto

```
SGG/
├── main.py                  # Punto de entrada de la aplicación Flask
├── requirements.txt         # Dependencias del proyecto
├── .env                     # Configuración de variables de entorno
├── app/
│   ├── __init__.py         # Inicialización de Flask, MongoDB y Blueprints
│   ├── models/             # Modelos de MongoEngine
│   ├── repositories/       # Capa de persistencia (Abstracción de DB)
│   ├── services/           # Lógica de negocio
│   ├── routes/             # Controladores de la API (Endpoints)
│   ├── utils/              # JWT Security, Handlers de Email
│   └── uploads/            # Almacenamiento de PDFs
├── tests/                   # Suite de pruebas automatizadas
│   ├── conftest.py         # Configuración y Fixtures de Pytest
│   ├── test_auth.py        # Pruebas de autenticación
│   ├── test_resources.py   # Pruebas de programas/regiones
│   ├── test_guides.py      # Pruebas de guías y archivos
│   └── test_e2e.py         # Flujos completos de integración
```

## Instalación y ejecución

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/maubry-ortega/SGG
   cd SGG
   ```
2. **Entorno Virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```
4. **Variables de Entorno (.env)**
   ```env
   SECRET_KEY=tu_clave_secreta_jwt
   MONGODB_URI=mongodb+srv://... (Tu conexión de Atlas)
   MONGODB_DB=sgg_db
   EMAIL_USER=tu_correo@gmail.com
   EMAIL_PASSWORD=tu_app_password
   ```
5. **Ejecutar**
   ```bash
   python main.py
   ```

## Pruebas Automatizadas

Para ejecutar las pruebas y verificar que todo funciona correctamente:

```bash
export PYTHONPATH=$PYTHONPATH:.
./venv/bin/python3 -m pytest -v tests/
```
*Las pruebas limpian automáticamente la base de datos de tests (`sgg_test_db`) al iniciar.*

## Endpoints de la API

| Método | Endpoint | Descripción | Protegido |
| :--- | :--- | :--- | :--- |
| POST | `/api/auth/login` | Login y obtención de JWT | No |
| GET | `/api/auth/me` | Obtener info del instructor actual | Sí |
| GET | `/api/guias/` | Listar todas las guías | No |
| POST | `/api/guias/` | Crear guía (Multipart/FormData) | Sí |
| POST | `/api/instructores/` | Registrar nuevo instructor | No |
| GET | `/api/regiones/` | Listar regiones | No |
| POST | `/api/programas/` | Crear programa | Sí |

## Tecnologías

- **Lenguaje**: Python 3.13+
- **Framework**: Flask
- **Autenticación**: PyJWT
- **Base de Datos**: MongoDB Atlas (MongoEngine)
- **Pruebas**: Pytest
- **Email**: Yagmail

---
**SGG API v2.0 - Desenvolvido por maubry-ortega**

