import logging
import ssl
from pathlib import Path

import torchvision

import iclearn.utils.transforms as tfs
from .dataloaders import DataLoaders
from .hitl import HitlSemanticSegmentationTorchDataset


class ImageDataLoaders(DataLoaders):
    def __init__(self, settings, cache_dir: Path, dataset_spec=None) -> None:
        super().__init__(settings, cache_dir, dataset_spec)

        transform_configs = self.config.get("transforms")
        self.transforms = tfs.from_config(transform_configs)

    def load_dataset(self):

        # Pytorch endpoint certs not maintained
        # https://github.com/pytorch/pytorch/issues/33288
        ssl._create_default_https_context = ssl._create_unverified_context

        if self.dataset_name == "eurosat":
            logging.info("Loading eurosat dataset")
            self.dataset = torchvision.datasets.EuroSAT(
                root=self.cache_dir, transform=self.transforms, download=True
            )
            logging.info("Finished loading eurosat dataset")
        elif self.dataset_name == "hitl_semantic_segmentation":
            logging.info("Loading hitl_semantic_segmentation dataset")
            self.dataset = HitlSemanticSegmentationTorchDataset(
                root=self.cache_dir, transforms=self.transforms
            )
            self.dataset.fetch()
            logging.info("Finished hitl_semantic_segmentation dataset")
        else:
            raise RuntimeError(
                f"Requested dataset name not supported {self.dataset_name}"
            )
