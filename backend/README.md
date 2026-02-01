# 🐙 SGG — Smart Guide Grid (Saggi)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/Neon-PostgreSQL-31C8CE?style=for-the-badge&logo=postgresql)](https://neon.tech/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb)](https://www.mongodb.com/)

**SGG (Smart Guide Grid)** es un motor backend modular de alto rendimiento diseñado para gobernar procesos administrativos y de aprendizaje. La plataforma expuesta a la comunidad se conoce como **Saggi**.

> "Construye conocimiento con sistema, no con caos."

## 🐙 Pulpo Ingeniero SGG

La mascota representa inteligencia multitarea, coordinación distribuida y ejecución paralela. Un solo cerebro (SGG Core), muchos brazos (Servicios Modulares).

## ✨ Características Clave

- **🎭 Un Cerebro, Dos Caras**: Branding dinámico para Comunidad (Saggi) vs Corporativo (SGG)
- **💾 Persistencia Híbrida**: Neon PostgreSQL (Gobernanza) + MongoDB Atlas (Grid de Recursos)
- **🔐 Seguridad JWT**: Tokens de Acceso/Refresco con bcrypt moderno
- **⚡ FastAPI Core**: Nativo asíncrono, tipado seguro y auto-documentado
- **🧪 Testing Completo**: Suite de pruebas con pytest y cobertura total
- **📦 Arquitectura Modular**: Separación clara de dominios y responsabilidades

## 🏗️ Arquitectura del Sistema

### Stack Tecnológico

- **Framework**: FastAPI 0.115+ (Python 3.13)
- **SQL Database**: Neon PostgreSQL (usuarios, gobernanza, auditoría)
- **NoSQL Database**: MongoDB Atlas (recursos de aprendizaje, comentarios)
- **Autenticación**: JWT con bcrypt
- **Storage**: Supabase Storage (archivos multimedia)
- **Testing**: pytest + httpx + pytest-asyncio

### Estructura del Proyecto

```
backend/
├── src/
│   ├── api/v1/              # Endpoints versionados
│   │   └── router.py        # Router principal API v1
│   ├── core/                # Configuración central
│   │   ├── config.py        # Variables de entorno
│   │   ├── database.py      # Conexiones SQL/NoSQL
│   │   └── security.py      # JWT y bcrypt
│   ├── modules/             # Módulos de dominio
│   │   ├── auth/            # Autenticación
│   │   ├── users/           # Gestión de usuarios
│   │   ├── governance/      # Regiones y programas
│   │   ├── learning/        # Recursos educativos (Saggi Grid)
│   │   └── branding/        # Branding dinámico
│   ├── shared/              # Código compartido
│   │   ├── models/          # Modelos de datos
│   │   └── utils/           # Utilidades (storage, email)
│   └── main.py              # Punto de entrada
├── tests/                   # Suite de pruebas
│   ├── conftest.py          # Fixtures de pytest
│   ├── test_v1_auth.py      # Tests de autenticación
│   ├── test_v1_governance.py
│   └── test_v1_learning.py
├── pytest.ini               # Configuración de pytest
├── requirements.txt         # Dependencias
└── .env                     # Variables de entorno
```

## 🚀 Inicio Rápido

### 1. Requisitos Previos

- Python 3.13+
- PostgreSQL (Neon) o local
- MongoDB Atlas o local
- Supabase account (opcional, para storage)

### 2. Configuración del Entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
# Database
SQLALCHEMY_DATABASE_URL=postgresql://user:password@host/database
MONGODB_URL=mongodb+srv://user:password@cluster.mongodb.net/
MONGODB_DB_NAME=saggi_db
MONGODB_TEST_DB_NAME=saggi_test_db

# JWT Security
SECRET_KEY=your-secret-key-here-min-32-chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Supabase Storage (opcional)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key

# Email (opcional)
EMAIL_USER=your-email@example.com
EMAIL_PASSWORD=your-app-password
```

### 3. Instalación

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 4. Ejecutar el Servidor

```bash
# Modo desarrollo (con auto-reload)
python3 -m uvicorn src.main:app --reload

# Modo producción
python3 -m uvicorn src.main:app --host 0.0.0.0 --port 8000
```

El servidor estará disponible en:
- **API**: http://localhost:8000
- **Documentación interactiva**: http://localhost:8000/docs
- **Documentación alternativa**: http://localhost:8000/redoc

## 📚 API Endpoints

### Base URL
```
http://localhost:8000/api/v1
```

### 🏥 Health Check

#### GET `/`
Verificar estado del servidor
```bash
curl http://localhost:8000/
```

**Respuesta:**
```json
{
  "message": "Welcome to SGG Smart Guide Grid (Saggi) Core Engine",
  "status": "Running",
  "docs": "/docs"
}
```

#### GET `/api/v1/health-grid`
Verificar estado del core grid
```bash
curl http://localhost:8000/api/v1/health-grid
```

**Respuesta:**
```json
{
  "status": "SGG Core Grid operational"
}
```

---

### 👥 Users (Usuarios)

#### POST `/api/v1/users/`
Crear un nuevo usuario

**Request Body:**
```json
{
  "full_name": "Juan Pérez",
  "email": "juan@example.com",
  "username": "juanperez",
  "password": "securepassword123",
  "role": "STUDENT",
  "identity": "COMMUNITY"
}
```

**Roles disponibles:** `STUDENT`, `INSTRUCTOR`, `ADMIN`  
**Identidades disponibles:** `COMMUNITY`, `CORPORATE`

**Ejemplo cURL:**
```bash
curl -X POST http://localhost:8000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "Juan Pérez",
    "email": "juan@example.com",
    "username": "juanperez",
    "password": "securepassword123"
  }'
```

**Respuesta (201 Created):**
```json
{
  "id": 1,
  "full_name": "Juan Pérez",
  "email": "juan@example.com",
  "username": "juanperez",
  "role": "STUDENT",
  "identity": "COMMUNITY",
  "created_at": "2026-01-31T03:00:00Z"
}
```

---

### 🔐 Auth (Autenticación)

#### POST `/api/v1/auth/login`
Iniciar sesión y obtener tokens JWT

**Request Body:**
```json
{
  "username": "juanperez",
  "password": "securepassword123"
}
```

**Ejemplo cURL:**
```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "juanperez",
    "password": "securepassword123"
  }'
```

**Respuesta (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "juanperez",
    "role": "STUDENT"
  }
}
```

**Respuesta de Error (401 Unauthorized):**
```json
{
  "detail": "Invalid credentials"
}
```

---

### 🏛️ Governance (Gobernanza)

#### POST `/api/v1/gov/regions`
Crear una nueva región

**Request Body:**
```json
{
  "name": "América Latina"
}
```

**Ejemplo cURL:**
```bash
curl -X POST http://localhost:8000/api/v1/gov/regions \
  -H "Content-Type: application/json" \
  -d '{"name": "América Latina"}'
```

**Respuesta (201 Created):**
```json
{
  "id": 1,
  "name": "América Latina"
}
```

#### GET `/api/v1/gov/regions`
Listar todas las regiones

```bash
curl http://localhost:8000/api/v1/gov/regions
```

**Respuesta:**
```json
[
  {
    "id": 1,
    "name": "América Latina"
  },
  {
    "id": 2,
    "name": "Europa"
  }
]
```

#### POST `/api/v1/gov/programs`
Crear un nuevo programa

**Request Body:**
```json
{
  "name": "Programa de Matemáticas Avanzadas"
}
```

**Ejemplo cURL:**
```bash
curl -X POST http://localhost:8000/api/v1/gov/programs \
  -H "Content-Type: application/json" \
  -d '{"name": "Programa de Matemáticas Avanzadas"}'
```

#### GET `/api/v1/gov/programs`
Listar todos los programas

```bash
curl http://localhost:8000/api/v1/gov/programs
```

---

### 📖 Learning (Saggi Grid - Recursos de Aprendizaje)

#### POST `/api/v1/learning/`
Crear un nuevo recurso educativo (con archivo)

**Request (multipart/form-data):**
- `title` (string): Título del recurso
- `description` (string): Descripción del recurso
- `instructor_id` (integer): ID del instructor
- `level` (string): Nivel (`BASIC`, `INTERMEDIATE`, `ADVANCED`)
- `tags` (array): Lista de etiquetas
- `file` (file): Archivo multimedia

**Ejemplo cURL:**
```bash
curl -X POST http://localhost:8000/api/v1/learning/ \
  -F "title=Introducción a Python" \
  -F "description=Curso básico de programación en Python" \
  -F "instructor_id=1" \
  -F "level=BASIC" \
  -F "tags=python" \
  -F "tags=programacion" \
  -F "file=@/path/to/video.mp4"
```

**Respuesta (201 Created):**
```json
{
  "id": "65f8a1b2c3d4e5f6a7b8c9d0",
  "title": "Introducción a Python",
  "description": "Curso básico de programación en Python",
  "instructor_id": 1,
  "level": "BASIC",
  "tags": ["python", "programacion"],
  "file_url": "https://storage.supabase.co/...",
  "created_at": "2026-01-31T03:00:00Z"
}
```

#### GET `/api/v1/learning/`
Listar todos los recursos educativos

```bash
curl http://localhost:8000/api/v1/learning/
```

**Respuesta:**
```json
[
  {
    "id": "65f8a1b2c3d4e5f6a7b8c9d0",
    "title": "Introducción a Python",
    "description": "Curso básico de programación en Python",
    "instructor_id": 1,
    "level": "BASIC",
    "tags": ["python", "programacion"],
    "file_url": "https://storage.supabase.co/...",
    "created_at": "2026-01-31T03:00:00Z"
  }
]
```

#### GET `/api/v1/learning/{id}`
Obtener un recurso específico por ID

```bash
curl http://localhost:8000/api/v1/learning/65f8a1b2c3d4e5f6a7b8c9d0
```

**Respuesta (200 OK):**
```json
{
  "id": "65f8a1b2c3d4e5f6a7b8c9d0",
  "title": "Introducción a Python",
  "description": "Curso básico de programación en Python",
  "instructor_id": 1,
  "level": "BASIC",
  "tags": ["python", "programacion"],
  "file_url": "https://storage.supabase.co/...",
  "created_at": "2026-01-31T03:00:00Z"
}
```

**Respuesta de Error (404 Not Found):**
```json
{
  "detail": "Resource not found"
}
```

---

## 🧪 Testing

El proyecto incluye una suite completa de pruebas con pytest.

### Ejecutar Todas las Pruebas

```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar pruebas
python -m pytest tests/ -v
```

### Ejecutar Pruebas Específicas

```bash
# Solo pruebas de autenticación
python -m pytest tests/test_v1_auth.py -v

# Solo pruebas de gobernanza
python -m pytest tests/test_v1_governance.py -v

# Solo pruebas de learning
python -m pytest tests/test_v1_learning.py -v
```

### Cobertura de Pruebas

```bash
python -m pytest tests/ --cov=src --cov-report=html
```

**Nota:** Las pruebas limpian automáticamente las bases de datos de prueba antes de cada ejecución.

---

## ⚛️ Integración con Frontend (React/Next.js)

### Configuración CORS

La API está configurada para aceptar peticiones de cualquier origen en desarrollo:

```python
allow_origins=["*"]  # Cambiar en producción
```

### Ejemplos de Consumo

#### Autenticación

```javascript
// Login
const login = async (username, password) => {
  const response = await fetch('http://localhost:8000/api/v1/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  
  if (!response.ok) {
    throw new Error('Invalid credentials');
  }
  
  const data = await response.json();
  // Guardar tokens en localStorage o state management
  localStorage.setItem('access_token', data.access_token);
  localStorage.setItem('refresh_token', data.refresh_token);
  
  return data;
};
```

#### Crear Usuario

```javascript
const registerUser = async (userData) => {
  const response = await fetch('http://localhost:8000/api/v1/users/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(userData)
  });
  
  return await response.json();
};
```

#### Obtener Recursos (con autenticación)

```javascript
const getResources = async () => {
  const token = localStorage.getItem('access_token');
  
  const response = await fetch('http://localhost:8000/api/v1/learning/', {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  
  return await response.json();
};
```

#### Subir Recurso con Archivo

```javascript
const uploadResource = async (formData) => {
  const token = localStorage.getItem('access_token');
  
  const response = await fetch('http://localhost:8000/api/v1/learning/', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`
    },
    body: formData  // FormData con file, title, description, etc.
  });
  
  return await response.json();
};
```

---

## 🔒 Seguridad

### Autenticación JWT

- **Access Token**: Expira en 30 minutos
- **Refresh Token**: Expira en 7 días
- **Algoritmo**: HS256
- **Hashing**: bcrypt con truncamiento a 72 bytes

### Mejores Prácticas Implementadas

✅ Contraseñas hasheadas con bcrypt moderno  
✅ Tokens JWT con expiración  
✅ Validación de entrada con Pydantic  
✅ Protección CORS configurable  
✅ Variables sensibles en `.env`  
✅ SQL injection prevention (SQLAlchemy ORM)  
✅ Separación de bases de datos de prueba

---

## 📊 Modelos de Datos

### SQL (PostgreSQL - Neon)

**User**
- `id`: Integer (PK)
- `full_name`: String
- `email`: String (unique)
- `username`: String (unique)
- `hashed_password`: String
- `role`: Enum (STUDENT, INSTRUCTOR, ADMIN)
- `identity`: Enum (COMMUNITY, CORPORATE)
- `created_at`: DateTime

**Region**
- `id`: Integer (PK)
- `name`: String

**Program**
- `id`: Integer (PK)
- `name`: String

### NoSQL (MongoDB Atlas)

**SaggiResource**
- `_id`: ObjectId
- `title`: String
- `description`: String
- `instructor_id`: Integer
- `level`: Enum (BASIC, INTERMEDIATE, ADVANCED)
- `tags`: Array[String]
- `file_url`: String
- `created_at`: DateTime

**Comment**
- `_id`: ObjectId
- `resource_id`: ObjectId
- `user_id`: Integer
- `content`: String
- `created_at`: DateTime

---

## 🚀 Despliegue

### Variables de Entorno en Producción

Asegúrate de configurar todas las variables en tu plataforma de hosting:

```env
SQLALCHEMY_DATABASE_URL=postgresql://...
MONGODB_URL=mongodb+srv://...
SECRET_KEY=<strong-random-key>
SUPABASE_URL=https://...
SUPABASE_KEY=...
```

### Comandos de Despliegue

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones (si aplica)
# alembic upgrade head

# Iniciar servidor
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

---

## 📝 Changelog

### v1.0.0 (2026-01-31)

- ✅ Sistema de autenticación JWT completo
- ✅ CRUD de usuarios con roles y permisos
- ✅ Gestión de regiones y programas (gobernanza)
- ✅ Sistema de recursos educativos con storage
- ✅ Suite completa de pruebas (pytest)
- ✅ Migración a bcrypt moderno (fix 72-byte limit)
- ✅ Actualización a SQLAlchemy 2.0
- ✅ Documentación API completa

---

## 🤝 Contribución

Este es un proyecto privado. Para contribuir, contacta al equipo de desarrollo.

---

## 📄 Licencia

Propietario: SGG Team  
Todos los derechos reservados.

---

**SGG Core Engine - Modular, Escalable, Inteligente.**

🐙 *Un cerebro, muchos brazos.*
