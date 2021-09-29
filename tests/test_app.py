import pytest

from app import create_app
from flask import json


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    return app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_alumnos(client):
    """Checando que se obtengan los dos alumnos"""

    alumnos = [
        {"nombre": "Jorge Alameda", "matricula": 15004131},
        {"nombre": "Axel Anaya", "matricula": 15004133 }
    ]

    # Convertimos el objeto de alumnos a byte
    json_alumnos = json.dumps(alumnos).encode('utf-8')
    rv = client.get('/alumnos/')

    assert json_alumnos == rv.data