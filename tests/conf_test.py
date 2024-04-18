import pytest
import json
from app.app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_healthz(client):
    response = client.get('/healthz')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'success'

