from fastapi import FastAPI

from ml_service.core_api.schemas import PredictResponse, PredictRequest
from ml_service.shared.services.base_transformer import CoreAPITransformer


class CoreAPI(FastAPI):
    def __init__(self, predict_transformer: CoreAPITransformer):
        super().__init__(swagger_ui_parameters={"displayRequestDuration": True})

        self.predict_transformer = predict_transformer
        self.setup_routers()

    def setup_routers(self):
        @self.post("/api/predict", response_model=list[PredictResponse])
        async def predict(input_body: PredictRequest):
            return await self.predict_transformer.invoke(input_body.input)
