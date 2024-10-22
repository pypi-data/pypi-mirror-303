"""
Testing dataset and metrics functionality.
"""

import os
from pathlib import Path
import torch
import numpy as np
import matplotlib.pyplot as plt

from mocks_linear import (
    LinearData,
    NoValidationLinearDataset,
    LinearMachineLearningModel,
    )

from icflow.utils import RuntimeContext
from iclearn.models import MetricsCalculator
from iclearn.output.logging_output_handler import LoggingOutputHandler
from iclearn.session.machine_learning import MachineLearningSession
from iccore.test_utils import get_test_data_dir


def plot_model(data_path):
    """Simply plots a loaded model against the training dataset.
    Reads from a standard *.pt model file, and compares with the .csv values of w and b
    created during data generation.

    :param data_path: A Path to the directory containing the model generated parameters
    :type data_path: Path
    """

    #create the paths
    model_path = data_path / "results/model.pt"
    param_path = data_path / "params"
    results_path = data_path / "results"

    #load the data
    model = torch.load(model_path, weights_only=False)

    w = np.genfromtxt(param_path / "w_rand.csv", delimiter=",", skip_header=0)
    b = np.genfromtxt(param_path / "b_rand.csv", delimiter=",", skip_header=0)

    x_train, y_train= np.genfromtxt(data_path / "train/train_data.csv", delimiter=",", skip_header=0, unpack=True, dtype=float)

    #plot the data
    plt.figure()
    plt.plot(x_train, (model["weight"].item() * x_train) + model["bias"].item(), color = "red", label = "iclearn Regression line")
    plt.plot(x_train, (w * x_train) + b, color = "black", label = "True parameter line")
    plt.scatter(x_train, y_train)
    plt.legend()

    plt.savefig(results_path / "iclearn.svg")



def plot_model_and_compare(data_path: Path, model_path: Path, param_path: Path, results_path: Path):
    """Compares the iclearn linear regression to the SEODA model parameters and the "real" line.

    Reads from .csv files and model.pt files.

    Plots the lines for rough comparison purposes.

    :param data_path: A path to x,y dataset.csv file.
    :type data_path: Path

    :param model_path: A path to the model.pt file.
    :type model_path: Path

    :param param_path: A path to the w (slope) and b (intercept).csv files. 
        Reads in both the "true" values and the SEODA model values.
    :type param_path: Path

    :param results_path: A path to where the comparison.png file will be saved.
    :type results_path: Path
    """

    #load the data
    model = torch.load(model_path, weights_only=False)

    w_rand = np.genfromtxt(param_path / "w_rand.csv", delimiter=",", skip_header=0)
    b_rand = np.genfromtxt(param_path / "b_rand.csv", delimiter=",", skip_header=0)

    w_real = np.genfromtxt(param_path / "w_real.csv", delimiter=",", skip_header=0)
    b_real = np.genfromtxt(param_path / "b_real.csv", delimiter=",", skip_header=0)

    x_test, y_test= np.genfromtxt(data_path / "train/train_data.csv", delimiter=",", skip_header=0, unpack=True, dtype=float)

    #plot the data
    plt.figure()
    plt.plot(x_test, (model["weight"].item() * x_test) + model["bias"].item(), color = "red", label = "iclearn Regression line")
    plt.plot(x_test, (w_rand * x_test) + b_rand, color = "green", label = "SEODA Regression line")
    plt.plot(x_test, (w_real * x_test) + b_real, color = "black", label = "True line")
    plt.scatter(x_test, y_test)
    plt.legend()

    plt.savefig(results_path / "comparison.svg")

# Generate the data and save.
def linear_data_generation(dim: int) -> Path:
    """A simple function to initialise and generate a LinearData class of points
        of size dim.

    Splits the data into 2/3 training, 1/6 validation, and 1/6 test.

    It saves the split data into the csv format specified in the 
        LinearData class' save function.

    :param dim: Defines the dimension/length of the (x, y) data array.
    :type dim: int
    """
    data = LinearData()
    data.generate(dim)

    train_bound = (2*len(data.x))//3
    val_bound = (len(data.x) - train_bound)//2

    data.split(train_bound, val_bound)

    work_dir = get_test_data_dir()
    dir = data.save(work_dir)
    return dir

def test_read_and_comp():
    """A function which begins a machine learning session using pre-existing data,
    saves the model, and the compares the model to another (SEODA) and to the 
    true (noiseless) line.
    
    Similar to the work in test_machine_learn
    """

    work_dir = get_test_data_dir()

    # First set up the runtime for the session, including the device (cpu/gpu)
    runtime = RuntimeContext()

    comparing = LinearData()
    comparing.read(work_dir / "comparing_data", is_split=False)
    comparing.split(101,0)
    comparing.as_tensors()
    dir = comparing.save(work_dir, params=False)

    # Create the SplitDataset class LinearDataset
    batch_size = 10
    dataset = NoValidationLinearDataset(dir, batch_size)

    # This metrics calculator is called after each batch prediction and can
    # be used to calculate and store metrics
    loss_func = torch.nn.MSELoss()
    metrics = MetricsCalculator(loss_func)
    
    # Collect anything 'model' related in a single object
    model = LinearMachineLearningModel(metrics)
 
    # This is a single machine learning 'experiment', which can be run distributed.
    # It takes the model and dataset and runs the requested 'stage'
    # 'test', 'train' etc.
    result_dir = work_dir / "results_compare"
    logging_output_handler = LoggingOutputHandler(result_dir)
    session = MachineLearningSession(model, runtime, result_dir, dataset)

    session.output_handlers.append(logging_output_handler)

    # Define the number of epochs and train the model
    num_epochs = 10
    session.train(num_epochs, val_dl_label="")

    # Save and plot the model
    model.save_model(result_dir)

    data_path = work_dir
    model_path=work_dir / "results_compare/model.pt"
    param_path= work_dir / "comparing_data"

    #This can be run to produce a plot comparing the "true line", the iclearn implementation, 
    # and the other model with different weights.

    plot_model_and_compare(data_path, model_path, param_path, result_dir)
