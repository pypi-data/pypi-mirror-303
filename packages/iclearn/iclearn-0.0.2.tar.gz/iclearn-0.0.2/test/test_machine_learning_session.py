import os
from pathlib import Path
import shutil

from mocks import (
    MockDataset,
    MockLossFunc,
    MockTorchDevice,
    MockMachineLearningModel,
    generate_mock_dataset,
)

from icflow.utils import RuntimeContext

from iclearn.models import MetricsCalculator
from iclearn.output.logging_output_handler import LoggingOutputHandler
from iclearn.session.machine_learning import MachineLearningSession


def test_machine_learning_session():

    work_dir = Path(os.getcwd())
    dataset_dir = generate_mock_dataset(work_dir)

    # First set up the runtime for the session, including the device (cpu/gpu)
    runtime = RuntimeContext()
    runtime.device = MockTorchDevice()

    # Give the path to the dataset, this will handle setting up
    # a Torch dataset, dataloaders and samplers as needed.
    batch_size = 5
    dataset = MockDataset(dataset_dir, batch_size)

    # This metrics calculator is called after each batch prediction and can
    # be used to calculate and store metrics for output to tensorboard,
    # mlflow, text logs or similar.
    loss_func = MockLossFunc()
    metrics = MetricsCalculator(loss_func)

    # Collect anything 'model' related in a single object
    model = MockMachineLearningModel(dataset.num_classes, metrics)

    # This is a single machine learning 'experiment', which can be run distributed.
    # It takes the model and dataset and runs the requested 'stage'
    # 'test', 'train' etc.
    result_dir = work_dir / "results"
    logging_output_handler = LoggingOutputHandler(result_dir)

    session = MachineLearningSession(model, runtime, result_dir, dataset)
    session.output_handlers.append(logging_output_handler)

    num_epochs = 1
    session.train(num_epochs)
    session.infer()

    shutil.rmtree(dataset_dir)
    shutil.rmtree(result_dir)
