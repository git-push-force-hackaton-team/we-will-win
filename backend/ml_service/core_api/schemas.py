from pydantic import BaseModel


class PredictRequest(BaseModel):
    input: str


class PredictResponse(BaseModel):
    start_index: int
    end_index: int
    entity: str
