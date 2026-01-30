import pytest
import json
from app.models.region import Region
from app.models.instructor import Instructor

def test_get_regiones(client):
    """Prueba que se puedan obtener las regiones"""
    response = client.get('/api/regiones/')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_crear_region(client, auth_header):
    """Prueba la creación de una región"""
    response = client.post('/api/regiones/',
                          data=json.dumps({"name": "Amazonas"}),
                          content_type='application/json',
                          headers=auth_header)
    assert response.status_code == 201
    assert response.json['name'] == 'Amazonas'


def test_get_programas(client):
    """Prueba que se puedan obtener los programas"""
    response = client.get('/api/programas/')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_crear_programa(client, auth_header):
    """Prueba la creación de un programa"""
    response = client.post('/api/programas/',
                          data=json.dumps({"name": "Nuevo Programa ADSO"}),
                          content_type='application/json',
                          headers=auth_header)
    assert response.status_code == 201
    assert response.json['name'] == 'Nuevo Programa ADSO'
