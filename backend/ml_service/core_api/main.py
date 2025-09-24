from dishka import make_container

from ml_service.core_api.application import CoreAPI
from ml_service.core_api.service_provider import make_core_api_service_provider

core_api = make_core_api_service_provider()
container = make_container(core_api)

app = container.get(CoreAPI)
