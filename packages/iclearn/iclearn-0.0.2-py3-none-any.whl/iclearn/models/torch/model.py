from pathlib import Path
import typing

import torch

from iclearn.models.metrics import MetricsCalculator
from iclearn.models.machine_learning_model import MachineLearningModel


class TorchModel(MachineLearningModel):
    """
    A machine learning model with PyTorch additions
    """

    def __init__(
        self,
        metrics_calculator: MetricsCalculator,
        model: typing.Any | None = None,
        model_path: Path | None = None,
        optimizer=None,
    ) -> None:

        super().__init__(metrics_calculator, model, model_path, optimizer)

        self.is_sent_to_device: bool = False

    def send_to_device(self) -> None:
        """
        Send the model to the compute device
        """

        if not self.is_sent_to_device:

            if not self.device:
                raise RuntimeError("Tried to send model to device but no device set")

            if not self.impl:
                raise RuntimeError("Tried to send model to device but no model set")

            self.impl.to(self.device.handle)
            self.is_sent_to_device = True

    def to_device(self, batch):

        if not self.device:
            raise RuntimeError("Tried to send batch to device, but no device set")

        return batch.to(self.device.handle)

    def load_from_file(self):
        """
        Load the model from the given path
        """

        if self.impl:
            return

        if not self.model_path:
            raise RuntimeError("Tried to load from file but no path set")

        self.impl = torch.load(self.model_path)

    def set_as_distributed(self) -> None:
        """
        If we are running distributed wrap torch model with ddp
        """

        if not self.impl:
            raise RuntimeError("Tried to set model as ddp, but no model loaded")
        self.impl = torch.nn.parallel.DistributedDataParallel(self.impl)

    def save(self, path):
        torch.save(self.impl.state_dict(), path)

    def on_epoch_start(self):

        torch.set_grad_enabled(True)
        super().on_epoch_start()

    def on_validation_start(self):
        torch.set_grad_enabled(False)
        super().on_validation_start()

    def on_before_infer(self):
        torch.set_grad_enabled(False)
        super().on_before_infer()
