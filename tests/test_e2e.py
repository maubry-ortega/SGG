import pytest
import json
from app.models.region import Region
from app.models.instructor import Instructor

def test_full_registration_and_login_flow(client):
    """
    Prueba el flujo completo:
    1. Crear una región necesaria.
    2. Registrar un instructor.
    3. Intentar login con las credenciales creadas.
    """
    # 1. Preparar datos (Región)
    region_name = "Cauca Test"
    region = Region(name=region_name).save()
    region_id = str(region.id)

    # 2. Registrar Instructor
    instructor_data = {
        "full_name": "Test User",
        "email": "test@sena.edu.co",
        "username": "testuser",
        "region": region_id
    }
    
    # El registro de instructor retorna el objeto instructor
    # Pero el endpoint /api/instructores/ POST retorna {"instructor": {...}}
    reg_response = client.post('/api/instructores/', 
                              data=json.dumps(instructor_data),
                              content_type='application/json')
    
    assert reg_response.status_code == 201
    reg_data = json.loads(reg_response.data)
    
    # En el servicio, la contraseña se genera aleatoriamente. 
    # Para los tests de login, necesitamos saber la contraseña o usar una fija.
    # Dado que el servicio la genera, podemos obtenerla de la DB para el test de login.
    instructor_db = Instructor.objects.get(username="testuser")
    password = instructor_db.password

    # 3. Intentar Login
    login_payload = {
        "username": "testuser",
        "password": password
    }
    login_response = client.post('/api/auth/login', 
                               data=json.dumps(login_payload),
                               content_type='application/json')
    
    assert login_response.status_code == 200
    login_data = json.loads(login_response.data)
    assert 'token' in login_data
    assert login_data['instructor']['username'] == "testuser"

    # 4. Validar acceso con Token (Ruta protegida /me)
    token = login_data['token']
    me_response = client.get('/api/auth/me', 
                            headers={"Authorization": f"Bearer {token}"})
    
    assert me_response.status_code == 200
    me_data = json.loads(me_response.data)
    assert me_data['username'] == "testuser"
