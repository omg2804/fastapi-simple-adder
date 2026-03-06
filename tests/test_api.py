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


def test_addition_large_numbers():
    response = client.post("/add", json={"a": 1e10, "b": 1e10})
    assert response.status_code == 200
    assert response.json() == {"result": 2e10}


def test_addition_float_numbers():
    response = client.post("/add", json={"a": 1.5, "b": 2.5})
    assert response.status_code == 200
    assert response.json() == {"result": 4.0}


def test_addition_empty_request():
    response = client.post("/add", json={})
    assert response.status_code == 422