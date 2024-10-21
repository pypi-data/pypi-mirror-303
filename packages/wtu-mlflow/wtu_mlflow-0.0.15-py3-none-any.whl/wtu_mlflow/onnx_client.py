import logging
import mlflow
import onnx
import json

# from onnx import ModelProto,
import os
from typing import Union

from mlflow.models.signature import infer_signature, ModelSignature
from mlflow.models.utils import ModelInputExample
from .base_mlflow_client import BaseMLflowClient
from .schema import Schema

"""
ModelInputExample
    mlflow 1.x 버전에서는 from mlflow.models.utils import ModelInputExample
    mlflow 2.x 버전에서는 from mlflow.models.signature import ModelInputExample
"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OnnxClient(BaseMLflowClient):
    def __init__(self):
        super().__init__()

    def upload(
        self,
        model: Union[onnx.ModelProto, str, bytes, os.PathLike],
        input_example: Schema,
        output_example: Schema,
    ):
        onnx.checker.check_model(model)

        if isinstance(model, (str, os.PathLike)):
            model = onnx.load(model)

        self._log_tensor(model)

        signature = infer_signature(
            model_input=input_example,
            model_output=output_example,
        )

        path = self._log_model(
            model=model,
            signature=signature,
            input_example=input_example,
        )

        if self.isProduction is False:
            return

        message = json.dumps({"train_id": self.train_id, "full_path": path})

        try:
            self.channel.basic_publish(
                exchange=self._uploadModelExchange,
                routing_key=self._uploadModelExchange,
                body=message,
            )
            logger.info("Model uploaded to RabbitMQ: %s", message)
        except Exception as e:
            logger.error("Failed to upload model to RabbitMQ: %s", e)

    def _log_tensor(self, onnx_model):
        """
        onnx.load 로 로드된 모델을 통해 input tensor와 output tensor의 정보를 출력합니다.
        """
        for input_tensor in onnx_model.graph.input:
            input_name = input_tensor.name

            input_type = self.get_triton_compatible_type(input_tensor.type.tensor_type)
            input_shape = [
                dim.dim_value for dim in input_tensor.type.tensor_type.shape.dim
            ]

            print(f"Input tensor name: {input_name}")
            print(f"Data type: {input_type}")
            print(f"Shape: {input_shape}")

        for output_tensor in onnx_model.graph.output:
            output_name = output_tensor.name
            output_type = self.get_triton_compatible_type(
                output_tensor.type.tensor_type
            )
            output_shape = [
                dim.dim_value for dim in output_tensor.type.tensor_type.shape.dim
            ]

            print(f"Output tensor name: {output_name}")
            print(f"Data type: {output_type}")
            print(f"Shape: {output_shape}")

    def _log_model(
        self,
        model,
        signature: ModelSignature,
        input_example: ModelInputExample,
    ) -> str:
        with mlflow.start_run():
            mlflow.onnx.log_model(
                onnx_model=model,
                artifact_path=self.model_name,
                signature=signature,
                input_example=input_example,
            )

            artifact_uri = mlflow.get_artifact_uri()
            model_full_path = f"{artifact_uri}/{self.model_name}"

            logger.info("Full path of the logged model: %s", model_full_path)
            return model_full_path
