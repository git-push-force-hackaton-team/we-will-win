from typing import TypedDict


class TransformerResponseType(TypedDict):
    start_index: int
    end_index: int
    entity: str
