import os
from pathlib import Path
import torch

from mocks_linear import (
    LinearData,
    LinearDataset,
    LinearMachineLearningModel,
    )

from test_linear_regression import plot_model

from icflow.utils import RuntimeContext
from iclearn.models import MetricsCalculator
from iclearn.output.logging_output_handler import LoggingOutputHandler
from iclearn.session.machine_learning import MachineLearningSession
from iccore.test_utils import get_test_data_dir


def test_machine_learning_regression_session():
    """This function contains the entire iclearn linear regression training session.
    We import the datasets and the machine learning model from mocks_linear.py. 

    The function trains the model and then saves it.
    It also produces plots of the model's line, the "true" noiseless line,
    and another model's line. (In this case the SEODA basic lin reg. example.)
    """

    work_dir = get_test_data_dir()

    # First set up the runtime for the session, including the device (cpu/gpu)
    runtime = RuntimeContext()

    # Generate the data
    data = LinearData()
    data.generate(dim=100)

    # Split the data into training, test, and validation data
    train_bound = (2*len(data.x))//3
    val_bound = (len(data.x) - train_bound)//2
    data.split(train_bound, val_bound)

    # Save the data and return the path
    dir = data.save(work_dir)

    # Create the SplitDataset class LinearDataset
    batch_size = 10
    dataset = LinearDataset(dir, batch_size)

    # This metrics calculator is called after each batch prediction and can
    # be used to calculate and store metrics.
    loss_func = torch.nn.MSELoss()
    metrics = MetricsCalculator(loss_func)
    
    # Collect anything 'model' related in a single object
    model = LinearMachineLearningModel(metrics)
 
    # This is a single machine learning 'experiment', which can be run distributed.
    # It takes the model and dataset and runs the requested 'stage'
    # 'test', 'train' etc.
    result_dir = work_dir / "results"
    logging_output_handler = LoggingOutputHandler(result_dir)
    session = MachineLearningSession(model, runtime, result_dir, dataset)

    session.output_handlers.append(logging_output_handler)

    # Define the number of epochs and train the model
    num_epochs = 10
    session.train(num_epochs)

    session.infer()

    # Save and plot the model
    model.save_model(result_dir)
    plot_model(work_dir)

