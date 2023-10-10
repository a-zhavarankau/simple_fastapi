import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_main():
    result = client.get("/")
    assert result.json() == "Hello from \'simple_fastapi\'"
