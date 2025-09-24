import pytest

from ml_service.core_api.application import CoreAPI
from ml_service.core_api.service_provider import make_core_api_service_provider
from dishka import make_container


@pytest.fixture(scope="session")
def core_api() -> CoreAPI:
    core_api_provider = make_core_api_service_provider()
    container = make_container(core_api_provider)
    return container.get(CoreAPI)
