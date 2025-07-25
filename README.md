# SGG - Sistema Gestor de Guías

SGG (Sistema Gestor de Guías) es una aplicación web desarrollada en Python con Flask y MongoDB, diseñada para la gestión eficiente de guías de aprendizaje, instructores, programas de formación y regiones. El sistema permite registrar, consultar y administrar guías en formato PDF, asociadas a instructores y programas, facilitando la organización y acceso a los materiales educativos.

## Características principales

- **Gestión de Guías de Aprendizaje**: Registro, listado, búsqueda, actualización y eliminación de guías en PDF.
- **Gestión de Instructores**: Registro de instructores con autenticación, asignación de región y generación automática de credenciales.
- **Gestión de Programas de Formación**: Alta, consulta, edición y eliminación de programas.
- **Gestión de Regiones**: Administración de regiones para segmentar instructores y programas.
- **Panel web moderno**: Interfaz responsiva y amigable, con tablas dinámicas, paginación y búsqueda en tiempo real.
- **Carga y descarga de archivos PDF**: Almacenamiento seguro de materiales de apoyo.
- **Notificaciones por correo**: Envío automático de credenciales a instructores registrados.
- **API RESTful**: Endpoints para integración y automatización de procesos.

## Estructura del proyecto

```
SGG/
├── main.py                  # Punto de entrada de la aplicación Flask
├── requirements.txt         # Dependencias del proyecto
├── app/
│   ├── __init__.py         # Inicialización y configuración de la app
│   ├── models/             # Modelos de datos (MongoEngine)
│   ├── repositories/       # Acceso a datos y lógica de persistencia
│   ├── services/           # Lógica de negocio
│   ├── routes/             # Rutas y controladores (API y vistas)
│   ├── static/             # Archivos estáticos (CSS, JS, iconos)
│   ├── templates/          # Plantillas HTML (Jinja2)
│   ├── utils/              # Utilidades (envío de emails, helpers)
│   └── uploads/            # Archivos PDF subidos
```

## Instalación y ejecución

1. **Clonar el repositorio**
   ```sh
   git clone https://github.com/maubry-ortega/SGG
   cd SGG
   ```
2. **Crear y activar un entorno virtual (opcional pero recomendado)**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Instalar dependencias**
   ```sh
   pip install -r requirements.txt
   ```
4. **Configurar variables de entorno**
   Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
   ```env
   SECRET_KEY=tu_clave_secreta
   MONGODB_URI=mongodb://localhost:27017/sgg_db
   MONGODB_DB=sgg_db
   EMAIL_USER=tu_correo@gmail.com
   EMAIL_PASSWORD=tu_contraseña
   ```
5. **Ejecutar la aplicación**
   ```sh
   python main.py
   ```
   La aplicación estará disponible en [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Endpoints principales

- `/api/guias/` - Listado y gestión de guías de aprendizaje
- `/api/instructores/` - Gestión de instructores
- `/api/programas/` - Gestión de programas de formación
- `/api/regiones/` - Gestión de regiones
- `/login` y `/registro` - Autenticación y registro de instructores
- `/guias/` - Vista web de guías

## Tecnologías utilizadas

- **Backend**: Python, Flask, Flask-CORS, Flask-Mail, Flask-WTF, MongoEngine, PyMongo
- **Frontend**: HTML5, CSS3, JavaScript (vanilla), Jinja2
- **Base de datos**: MongoDB
- **Otros**: Dotenv, Yagmail (envío de emails), Gunicorn (despliegue)

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

**Desarrollado por maubry-ortega**

Para dudas, sugerencias o contribuciones, abre un issue o contacta al autor.
