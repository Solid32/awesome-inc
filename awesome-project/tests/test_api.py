import pytest
from fastapi.testclient import TestClient


from src.api import app
from src.params import ALLOWED_TABLES

client = TestClient(app)
class TestBase: 

    def test_tables(self):
        for table in ALLOWED_TABLES:
            response = client.get(f"/api/{table}")
            assert response.status_code == 200

    def test_response_format(self):
        for table in ALLOWED_TABLES:
            response = client.get(f"/api/{table}")
            assert response.headers["content-type"] == "application/json"
