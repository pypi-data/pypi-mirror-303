
import sys
import os

import pytest
from fastapi.testclient import TestClient
from moto import mock_aws
from unittest.mock import MagicMock,patch
#from moto import mock_secretsmanager
import boto3
import json
from app.utils import config
from app.main import app

client = TestClient(app)

#class TestSuccessfulResponse:
    
#valid input
def test_uppercase_data():
    payload = {
        "name":"harry",
        "input": "harry"
    }
    response = client.post("/upper_input_payload",json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["requestor_name"] == payload["input"]
    assert data["upper_input"] == payload["name"].upper()


@pytest.mark.asyncio
async def test_retrieve_secret():
    # Mock the boto3 client and its get_secret_value method
    with patch("boto3.client") as mock_boto_client:
        mock_secrets_manager = mock_boto_client.return_value
        mock_secrets_manager.get_secret_value.return_value = {
            "SecretString": '{"username": "test_user", "password": "test_pass"}'
        }
        response = client.get("/retrive_secrets/?name=test")
        assert response.status_code == 200
        assert response.json() == {
            "name": "test",
            "message": "Secret retrived successfully"
        }


class TestErrorHandling:
    def test_uppercase_data_invalid_name_type(self):
        response = client.post("/upper_input_payload", json={"name": 1234, "input": "hello"})
        assert response.status_code == 400
        assert response.json() == {"detail": "Input cannot be empty. Please provide a valid string."}

    def test_uppercase_data_invalid_input_type(self):
        response = client.post("/upper_input_payload", json={"name": "hello", "input": 1234 })
        assert response.status_code == 400
        assert response.json() == {"detail": "Input cannot be empty. Please provide a valid string."}

    def test_uppercase_data_empty_name(self):
        response = client.post("/upper_input_payload", json={"name": "", "input": "hello"})
        assert response.status_code == 400
        assert response.json() == {"detail": "Input cannot be empty. Please provide a valid string."}

    def test_uppercase_data_empty_input(self):
        response = client.post("/upper_input_payload", json={"name": "John", "input": ""})
        assert response.status_code == 400
        assert response.json() == {"detail": "Input cannot be empty. Please provide a valid string."}

    def test_retrive_secret_invalid_parameter(self):
        response = client.get("/retrive_secrets/?nam=sonal")
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_retrieve_secret_failure():
        with patch("boto3.client") as mock_boto_client:
            mock_secrets_manager = mock_boto_client.return_value
            mock_secrets_manager.get_secret_value.side_effect = Exception("Secrets Manager error")
            response = client.get("/retrive_secrets/?name=test")
            assert response.status_code == 500
            assert "Internal Server Error" in response.json()["detail"]