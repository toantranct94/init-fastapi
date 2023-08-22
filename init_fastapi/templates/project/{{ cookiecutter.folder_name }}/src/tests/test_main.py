from app.main import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_health(test_app):
    # Arrange

    # Act
    response = client.get("/api/health")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
