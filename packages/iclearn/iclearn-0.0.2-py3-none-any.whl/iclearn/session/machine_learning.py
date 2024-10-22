"""
This module has functionality for Machine Learning workflows
"""

import logging
from pathlib import Path

from icflow.utils.runtime import RuntimeContext
from icflow.data import SplitDataset
from icflow.session import WorkflowSession

from iclearn.models import MachineLearningModel
from iclearn.output import OutputHandler

logger = logging.getLogger(__name__)


class MachineLearningSession(WorkflowSession):
    """
    This is a Machine Learning workflow session
    """

    def __init__(
        self,
        model: MachineLearningModel,
        runtime_ctx: RuntimeContext,
        result_dir: Path = Path(),
        dataset: SplitDataset | None = None,
    ) -> None:
        super().__init__(result_dir, runtime_ctx)

        self.model = model
        self.runtime_ctx = runtime_ctx
        self.model.device = self.runtime_ctx.device
        self.model.metrics.cache.runtime_ctx = self.runtime_ctx
        self.dataset = dataset
        if self.dataset:
            self.dataset.runtime_ctx = runtime_ctx
        self.output_handlers: list[OutputHandler] = []
        self.last_predictions = None

    def do_batch(self, batch, update_optimizer: bool = False) -> bool:
        """
        Operate on a single batch. The 'update_optimizer'
        flag should be True in the test stage.
        """

        self.on_batch_start()

        if update_optimizer:
            self.model.optimizer.zero_grad()

        x = self.model.to_device(batch[0])
        y = self.model.to_device(batch[1])
        prediction = self.model.predict(x)
        loss = self.model.calculate_loss(prediction, y)

        if update_optimizer:
            loss.backward()
            self.model.optimizer.step()
        return self.on_batch_end(prediction, y)

    def on_before_epochs(self, num_epochs: int):
        """
        Called before the epoch loop starts
        """

        self.runtime_ctx.init()

        if not self.dataset:
            raise RuntimeError("Tried to train without dataset")
        self.dataset.load()

        self.model.on_before_epochs(self.runtime_ctx.is_multigpu)
        for handler in self.output_handlers:
            handler.on_before_epochs(num_epochs, self.dataset)

    def on_after_epochs(self):
        """
        Called when all epochs are completed
        """
        for handler in self.output_handlers:
            handler.on_after_epochs()

    def on_epoch_start(self, epoch_idx: int):
        """
        Called at the beginning of an epoch
        """
        self.model.on_epoch_start()
        if self.dataset:
            self.dataset.on_epoch_start(epoch_idx)

        for handler in self.output_handlers:
            handler.on_epoch_start(self.get_num_train_batches())

    def on_epoch_end(self):
        """
        Called at the end of an epoch
        """
        should_save, should_finish = self.model.on_epoch_end()
        for handler in self.output_handlers:
            handler.on_epoch_end(self.model.metrics.cache)

        if should_save and self.runtime_ctx.is_master_process():
            logger.info("Saving model with best loss value.")
            self.output_handlers.save_model(self.model)

        if should_finish:
            logger.info("Stopping training due to stop criterion.")
            return True
        return False

    def on_batch_start(self):
        """
        Called at the start of a batch, before any predicionts
        """
        self.model.on_batch_start()
        for handler in self.output_handlers:
            handler.on_batch_start()

    def on_batch_end(self, prediction, ground_truth) -> bool:
        """
        Called at the end of a batch, after predictions
        """
        should_break = self.model.on_batch_end(prediction, ground_truth)
        for handler in self.output_handlers:
            handler.on_batch_end(self.model.metrics.cache)
        return should_break

    def get_num_train_batches(self):
        """
        Covenience method to get number of training batches
        """
        return self.dataset.get_num_batches("train")

    def get_num_val_batches(self):
        """
        Convenience method to get number of validation batches
        """
        return self.dataset.get_num_batches("val")

    def on_validation_start(self):
        """
        Called after training epochs, at the start of the
        validation stage.
        """
        self.model.on_validation_start()
        for handler in self.output_handlers:
            handler.on_validation_start()

    def do_batches(self, dl_label: str, update_optimizer: bool = False):
        """
        Loop over all batches in the labelled dataloader
        """

        if not self.dataset:
            raise RuntimeError("Tried to process batch with no dataset")

        for batch in self.dataset.get_dataloader(dl_label):
            should_break = self.do_batch(batch, update_optimizer)
            if should_break:
                logger.info("Breaking from batch loop early")
                break

    def train(
        self,
        num_epochs: int,
        train_dl_label: str = "train",
        val_dl_label: str = "val",
    ):
        """
        Run the training stage
        """

        self.on_before_epochs(num_epochs)
        for epoch in range(1, num_epochs + 1):
            self.on_epoch_start(epoch)
            self.do_batches(train_dl_label, update_optimizer=True)

            if val_dl_label != "":
                self.on_validation_start()
                self.do_batches(val_dl_label)
            else:
                continue

            should_break = self.on_epoch_end()
            if should_break:
                break

        self.on_after_epochs()

    def on_before_infer(self):
        """
        Called before attempting to do inference
        """
        self.runtime_ctx.init()
        if not self.dataset:
            raise RuntimeError("Tried to do inference with no input data")
        self.dataset.load()
        self.model.on_before_infer()

    def on_after_infer(self, stage):
        """
        Called after doing inference
        """

        for handler in self.output_handlers:
            handler.on_after_infer(
                stage, self.last_predictions, self.model.metrics.cache
            )

    def infer(self, test_dl_label: str = "test"):
        """
        Run the model in inference mode
        """

        self.on_before_infer()
        self.do_batches(test_dl_label)
        self.on_after_infer(test_dl_label)
