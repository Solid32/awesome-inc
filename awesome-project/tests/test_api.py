import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
import asyncio

from src.api import app, DataApi
from src.params import ALLOWED_TABLES

class TestBase: 

    def test_tables_name(self):
        client = TestClient(app)
        for table in ALLOWED_TABLES:
            response = client.get(f"/api/{table}")
            assert response.status_code == 200
        response = client.get("api/test")
        assert response.status_code == 404

    def test_response_format_json(self):
        client = TestClient(app)
        for table in ALLOWED_TABLES:
            response = client.get(f"/api/{table}")
            assert response.headers["content-type"] == "application/json"
