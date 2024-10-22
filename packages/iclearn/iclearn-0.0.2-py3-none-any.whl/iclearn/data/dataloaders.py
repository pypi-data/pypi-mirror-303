import logging
from pathlib import Path
import os

from torch.utils.data import DataLoader, random_split

from icflow.data.dataset_collection import DatasetCollection

from iclearn.utils.serialization import Config


class DataLoaders:
    def __init__(
        self, config: Config, cache_dir: Path, dataset_path: Path | None = None
    ) -> None:
        self.config = config
        self.cache_dir = cache_dir
        self.dataset_name = config.get("dataset_name")
        self.transforms = config.get("transforms")
        if dataset_path is not None:
            self.load_dataset_collection(dataset_path)
        self.batch_size = config.get("batch_size", 64)
        self.splits = config.get("train_val_split", [0.9, 0.05])
        self.num_workers = config.get("num_dataloader_workers", 1)
        self.dataset = None
        self.train_dataloader = None
        self.test_dataloader = None
        self.val_dataloader = None

    def get_num_classes(self):
        return len(self.dataset.classes)

    def load_dataset_collection(self, path):
        self.dataset_collection = DatasetCollection(path)
        self.dataset_collection.load()

    def fetch(self):
        if os.path.exists(self.cache_dir / self.dataset_name):
            return
        self.dataset_collection.download_item(self.dataset_name, self.cache_dir)

    def get_splits(self):
        training_len = int(len(self.dataset) * self.splits[0])
        if len(self.splits) == 1:
            validation_len = 0
        else:
            validation_len = int(len(self.dataset) * self.splits[1])
        test_len = len(self.dataset) - (training_len + validation_len)
        return [training_len, validation_len, test_len]

    def load(self):
        logging.info("Preparing dataloaders")
        self.load_dataset()
        splits = self.get_splits()
        if splits[2] == 0:
            train_dataset, val_dataset = random_split(self.dataset, splits[0:2])
            test_dataset = None
        else:
            train_dataset, val_dataset, test_dataset = random_split(
                self.dataset, splits
            )

        self.train_dataloader = DataLoader(
            train_dataset,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.num_workers,
        )
        self.val_dataloader = DataLoader(
            val_dataset,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=self.num_workers,
        )
        if test_dataset is not None:
            self.test_dataloader = DataLoader(
                test_dataset,
                batch_size=self.batch_size,
                shuffle=False,
                num_workers=self.num_workers,
            )

        self.summarize_datasets()
        logging.info("Finished Preparing dataloaders")

    def summarize_datasets(self):
        num_test = 0
        if self.test_dataloader is not None:
            num_test = len(self.test_dataloader)
        train_counts = f"Train {len(self.train_dataloader)}"
        valid_counts = f"Validation {len(self.val_dataloader)}"
        test_counts = f"Test {num_test}"
        logging.info(
            f"Dataset counts | {train_counts} - {valid_counts} - {test_counts}"
        )
