import pytest

from ml_service.core_api.application import CoreAPI
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def client(core_api: CoreAPI) -> TestClient:
    return TestClient(core_api)
