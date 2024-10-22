import logging

import torch

from icflow.utils.devices import ComputeDevice

logger = logging.getLogger(__name__)


class TorchComputeDevice(ComputeDevice):
    """
    This represents a compute device, such as a GPU or CPU
    """

    def load(self):
        if torch.cuda.is_available():
            self.name = f"cuda:{self.local_rank}"
        logger.info("Loading torch device %s", self.name)
        self.handle = torch.device(self.name)
