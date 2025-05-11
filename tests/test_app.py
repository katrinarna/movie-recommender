import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_recommend_endpoint_success(client):
    response = client.get('/recommend?title=Inception')
    data = response.get_json()
    assert response.status_code == 200
    assert "recommendations" in data
    assert len(data["recommendations"]) == 5

def test_recommend_endpoint_failure(client):
    response = client.get('/recommend?title=SomeFakeTitle')
    data = response.get_json()
    assert response.status_code == 200
    assert "error" in data

def test_recommend_endpoint_empty(client):
    response = client.get('/recommend?title=')
    data = response.get_json()
    assert response.status_code == 200
    assert "error" in data
