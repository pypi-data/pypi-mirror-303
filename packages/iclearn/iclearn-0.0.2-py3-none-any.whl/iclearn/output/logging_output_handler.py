"""
This module supports output via a logger
"""

import logging
import time

from icflow.data import SplitDataset

from iclearn.models import MetricsCache
from .output_handler import OutputHandler

logger = logging.getLogger(__name__)


class LoggingOutputHandler(OutputHandler):
    """
    This class implements output handling via a logger.
    """

    def on_before_epochs(self, num_epochs: int, split_dataset: SplitDataset):
        super().on_before_epochs(num_epochs, split_dataset)
        logger.info("Start training with %s epochs", self.num_epochs)

    def on_after_epochs(self):
        super().on_after_epochs()
        logger.info(
            "Training finished in %0.3f minutes",
            self.get_elapsed_time(self.start_time) / 60,
        )

    def on_epoch_start(self, num_batches: int):
        super().on_epoch_start(num_batches)
        logger.info("Starting Epoch [%s/%s]", self.epoch_count, self.num_epochs)

    def on_epoch_end(self, metrics: MetricsCache):
        super().on_epoch_end(metrics)

        delta_time = time.time() - self.start_time
        # if self.use_tensorboard:
        # self.tb_writer.add_scalar(msg, scalar, epoch_count)
        logger.info(
            "Finished Epoch [%s/%s]. Results:", self.epoch_count, self.num_epochs
        )
        for line in self.serialize_metrics(delta_time, metrics):
            logging.info(line)

        logger.info("Epoch %s training results", self.epoch_count)
        logger.info("Time %0.3f", self.get_elapsed_time(self.epoch_start_time))
        self.log_step_results(metrics, self.epoch_count)

    def on_batch_start(self):
        super().on_batch_start()
        logger.info("Starting batch %s/%s", self.batch_count, self.num_batches)

    def on_batch_end(self, metrics: MetricsCache):
        super().on_batch_end(metrics)
        loss = metrics.batch_last_results["loss"]
        logger.info("Finished Batch %d, loss: %0.4f", self.batch_count, loss)

    def on_validation_start(self):
        super().on_validation_start()
        logger.info("Start validating epoch: %s", self.epoch_count)

    def on_after_infer(self, stage, predictions, metrics: MetricsCache):
        super().on_after_infer(stage, predictions, metrics)
        self.log_dict_results(stage, metrics)

    def serialize_metrics(self, delta_time, metrics: MetricsCache):
        lines = []
        lines.append(f"Train time {delta_time:.3f} secs")
        for stage, results in metrics.stage_results.items():
            for key, value in results.items():
                lines.append(f"{stage} {key} -> {value}")
        return lines

    def log_dict_results(self, prefix, metrics: MetricsCache):
        for key, value in metrics.stage_results.items():
            logger.info("%s: %0.4f", f"{prefix}_{key}", value)

    def log_step_results(self, metrics: MetricsCache, step: int):
        """
        Log results to file and if present, mlflow
        """

        for stage, values in metrics.stage_results.items():
            for metric_key, metric_values in values.items():
                logger.info(
                    "%s %s -> %0.3f", stage, metric_key, metric_values[step - 1]
                )
