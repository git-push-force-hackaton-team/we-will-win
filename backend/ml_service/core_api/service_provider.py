from dishka import Provider, Scope

from ml_service.core_api.application import CoreAPI
from ml_service.shared.services.base_transformer import CoreAPITransformer
from ml_service.shared.services.real_transformer import A


def make_core_api_service_provider():
    service_provider = Provider(scope=Scope.APP)
    service_provider.provide(CoreAPI)
    service_provider.provide(A, provides=CoreAPITransformer)
    return service_provider
