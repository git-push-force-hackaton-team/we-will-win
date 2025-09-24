from ml_service.shared.services.base_transformer import CoreAPITransformer
from ml_service.shared.types.core_response_types import TransformerResponseType


class A(CoreAPITransformer):
    async def invoke(self, text: str) -> list[TransformerResponseType]:
        resp: TransformerResponseType = {
            "start_index": 0,
            "end_index": len(text),
            "entity": "I-TYPE",
        }
        return [resp]
