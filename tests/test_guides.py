import pytest
import json
import io
from app.models.program import ProgramaFormacion
from app.models.instructor import Instructor
from app.models.region import Region

@pytest.fixture
def instructor_from_auth(auth_header):
    """Extrae el instructor de la base de datos basándose en el fixture compartido"""
    from app.models.instructor import Instructor
    return Instructor.objects.get(username="testuser_fixture")

def test_listar_guias_empty(client):
    """Prueba listar guías cuando no hay ninguna"""
    response = client.get('/api/guias/')
    assert response.status_code == 200
    assert response.json == []

def test_crear_guia_success(client, auth_header):
    """Prueba la creación exitosa de una guía"""
    from app.models.program import ProgramaFormacion
    import io

    # Necesitamos un programa
    programa = ProgramaFormacion(name="ADSO Test").save()

    # Simulamos un archivo PDF
    data = {
        'full_name': 'Guía de Pruebas API',
        'description': 'Descripción de la guía de pruebas',
        'program': str(programa.id),
        'archivo': (io.BytesIO(b"contenido pdf falso"), 'test.pdf')
    }

    response = client.post('/api/guias/',
                          data=data,
                          content_type='multipart/form-data',
                          headers=auth_header)

    assert response.status_code == 201
    assert response.json['full_name'] == 'Guía de Pruebas API'

def test_crear_guia_invalid_data(client, auth_header):
    """Prueba la creación con datos faltantes"""
    # auth_header ya es un diccionario {"Authorization": "Bearer ..."}
    
    data = {

        'full_name': '', # Faltan campos
        'archivo': (io.BytesIO(b"contenido pdf"), 'test.pdf')
    }
    response = client.post('/api/guias/',
                          data=data,
                          content_type='multipart/form-data',
                          headers=auth_header)
    assert response.status_code == 400
    assert 'error' in response.json
