from abc import ABC, abstractmethod

from ml_service.shared.types.core_response_types import TransformerResponseType


class CoreAPITransformer(ABC):
    @abstractmethod
    async def invoke(self, text: str) -> list[TransformerResponseType]:
        raise NotImplementedError
