import pytest
import os
from mongoengine import connect, disconnect

@pytest.fixture(scope='session')
def app():
    # Mockeamos yagmail ANTES de cualquier importación de la app
    from unittest.mock import patch
    with patch('yagmail.SMTP') as mock_smtp:
        # Ahora importamos create_app
        from app import create_app
        
        # Desconectamos cualquier conexión existente para evitar conflictos
        disconnect(alias='default')
        
        # Configuramos variables de entorno para pruebas
        os.environ['MONGODB_DB'] = 'sgg_test_db'
        os.environ['MONGODB_URI'] = "mongodb+srv://sena2025:sena2025@cluster0.b63fae2.mongodb.net/?appName=Cluster0"
        
        _app = create_app()
        _app.config.update({
            "TESTING": True,
        })
        
        # Limpiamos la base de datos de prueba al inicio para asegurar un estado limpio
        from mongoengine.connection import get_db
        db = get_db()
        db.client.drop_database('sgg_test_db')
        
        yield _app
        
        # Limpieza final
        disconnect(alias='default')



@pytest.fixture(scope='session', autouse=True)
def mock_yagmail(session_mocker=None):
    """Mockea yagmail para evitar envíos reales y esperas"""
    try:
        from unittest.mock import patch
        with patch('yagmail.SMTP') as mock:
            yield mock
    except ImportError:
        yield None

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def auth_header(client):
    """Fixture para obtener un header con token JWT válido"""
    from app.models.region import Region
    from app.models.instructor import Instructor
    
    # 1. Crear región si no existe
    region = Region.objects(name="Test Region Fixture").first()
    if not region:
        region = Region(name="Test Region Fixture").save()
    
    # 2. Registrar instructor si no existe
    username = "testuser_fixture"
    password = "password123"
    instructor = Instructor.objects(username=username).first()
    if not instructor:
        instructor_data = {
            "full_name": "Fixture User",
            "email": "fixture@sena.edu.co",
            "username": username,
            "password": password,
            "region": str(region.id)
        }
        client.post('/api/instructores/', json=instructor_data)
    
    # 3. Login
    login_res = client.post('/api/auth/login', json={"username": username, "password": password})
    if login_res.status_code != 200:
        raise Exception(f"Login failed in fixture: {login_res.data}")
        
    token = login_res.json.get('token')
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture(scope='function')
def runner(app):
    return app.test_cli_runner()
