import pytest
from fastapi.testclient import TestClient
from src.app import app

# Arrange-Act-Assert pattern

def test_root_endpoint():
    # Arrange
    client = TestClient(app)
    # Act
    response = client.get("/", follow_redirects=False)
    # Assert
    assert response.status_code in (302, 307)  # Redirect
    assert response.headers["location"].endswith("/static/index.html")
