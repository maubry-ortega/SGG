import pytest
import json

def test_login_no_payload(client):
    """Prueba que el login falle sin datos"""
    response = client.post('/api/auth/login', 
                          data=json.dumps({}),
                          content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'mensaje' in data

def test_login_invalid_credentials(client):
    """Prueba que el login falle con credenciales incorrectas"""
    response = client.post('/api/auth/login', 
                          data=json.dumps({
                              "username": "usuario_no_existe",
                              "password": "wrong_password"
                          }),
                          content_type='application/json')
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['mensaje'] == "Usuario o contraseña incorrectos"

def test_me_without_token(client):
    """Prueba que /me falle sin token"""
    response = client.get('/api/auth/me')
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == "Token faltante"
