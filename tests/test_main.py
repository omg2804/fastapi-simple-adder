import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_addition():
    response = client.post("/add", json={"a": 1, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_addition_negative_numbers():
    response = client.post("/add", json={"a": -1, "b": -2})
    assert response.status_code == 200
    assert response.json() == {"result": -3}

def test_addition_zero():
    response = client.post("/add", json={"a": 0, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"result": 0}

def test_addition_invalid_input():
    response = client.post("/add", json={"a": "one", "b": 2})
    assert response.status_code == 422