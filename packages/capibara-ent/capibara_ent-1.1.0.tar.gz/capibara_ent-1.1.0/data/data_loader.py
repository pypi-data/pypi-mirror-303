"""
Module for loading multilingual data for the CapibaraGPT model.

This module provides a class to create and manage DataLoaders
for training, validation, and test datasets in multiple languages.

Classes:
    Config: Configuration class for data loading parameters.
    MultilingualDataLoader: Manages the loading of multilingual data.

Dependencies:
    - torch: For DataLoader functionality.
    - .multilingual_dataset: For the MultilingualDataset class.
"""

import logging
from pathlib import Path
from typing import Dict, Optional, List
import torch
from torch.utils.data import DataLoader
from .multilingual_dataset import MultilingualDataset
import os
from dotenv import load_dotenv
import json

logger = logging.getLogger(__name__)


class Config:
    def __init__(self, **kwargs):
        load_dotenv()
        self.train_data_path = kwargs.get('train_data_path') or os.path.join(
            os.getenv('CAPIBARA_DATA_PATH'), 'train')
        self.val_data_path = kwargs.get('val_data_path') or os.path.join(
            os.getenv('CAPIBARA_DATA_PATH'), 'val')
        self.test_data_path = kwargs.get('test_data_path') or os.path.join(
            os.getenv('CAPIBARA_DATA_PATH'), 'test')
        self.batch_size = int(kwargs.get('batch_size')
                              or os.getenv('CAPIBARA_BATCH_SIZE'))
        self.max_length = int(kwargs.get('max_length')
                              or os.getenv('CAPIBARA_MAX_LENGTH'))
        self.supported_languages = kwargs.get('supported_languages') or os.getenv(
            'CAPIBARA_SUPPORTED_LANGUAGES', 'es,en,pt').split(',')
        self.num_workers = int(kwargs.get('num_workers')
                               or os.getenv('CAPIBARA_NUM_WORKERS', '4'))
        self.use_cache = kwargs.get('use_cache') or os.getenv(
            'CAPIBARA_USE_CACHE', 'false').lower() == 'true'
        self.data_format = kwargs.get('data_format') or os.getenv(
            'CAPIBARA_DATA_FORMAT', 'json')


class MultilingualDataLoader:
    def __init__(self, config: Config):
        self.config = config
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        logger.info("Initializing MultilingualDataLoader...")
        self._validate_config()
        self._validate_data_paths()
        self._initialize_datasets()

    def _validate_config(self):
        required_attributes = ['train_data_path', 'val_data_path', 'test_data_path',
                               'supported_languages', 'batch_size', 'num_workers']
        for attr in required_attributes:
            if not hasattr(self.config, attr):
                raise AttributeError(f"Config object must contain '{
                                     attr}' attribute.")
        if not isinstance(self.config.num_workers, int) or self.config.num_workers < 0:
            raise ValueError(
                "Number of workers must be a non-negative integer.")

    def _validate_data_paths(self):
        for path_attr in ['train_data_path', 'val_data_path', 'test_data_path']:
            path = getattr(self.config, path_attr)
            if not Path(path).exists():
                raise FileNotFoundError(f"Data path '{path}' does not exist.")

    def _initialize_datasets(self):
        try:
            self.train_dataset = MultilingualDataset(self.config.train_data_path, self.config.supported_languages,
                                                     data_format=self.config.data_format, use_cache=self.config.use_cache)
            self.val_dataset = MultilingualDataset(self.config.val_data_path, self.config.supported_languages,
                                                   data_format=self.config.data_format, use_cache=self.config.use_cache)
            self.test_dataset = MultilingualDataset(self.config.test_data_path, self.config.supported_languages,
                                                    data_format=self.config.data_format, use_cache=self.config.use_cache)
        except Exception as e:
            raise RuntimeError(f"Error initializing dataset: {e}")

        for dataset_name, dataset in [("training", self.train_dataset),
                                      ("validation", self.val_dataset),
                                      ("test", self.test_dataset)]:
            if len(dataset) == 0:
                raise ValueError(f"The {dataset_name} dataset is empty.")
            logger.info(f"{dataset_name.capitalize()
                           } dataset size: {len(dataset)}")

    def _create_loader(self, dataset, batch_size, shuffle):
        sampler = None
        if torch.distributed.is_initialized():
            sampler = torch.utils.data.distributed.DistributedSampler(dataset)
            shuffle = False

        return DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=shuffle,
            num_workers=self.config.num_workers,
            pin_memory=True,
            prefetch_factor=2,
            sampler=sampler
        )

    def get_train_loader(self, batch_size: Optional[int] = None) -> DataLoader:
        batch_size = batch_size or self.config.batch_size
        logger.info(
            f"Creating training DataLoader with batch size {batch_size}")
        return self._create_loader(self.train_dataset, batch_size, shuffle=True)

    def get_val_loader(self, batch_size: Optional[int] = None, shuffle: bool = False) -> DataLoader:
        batch_size = batch_size or self.config.batch_size
        logger.info(
            f"Creating validation DataLoader with batch size {batch_size}")
        return self._create_loader(self.val_dataset, batch_size, shuffle=shuffle)

    def get_test_loader(self, batch_size: Optional[int] = None, shuffle: bool = False) -> DataLoader:
        batch_size = batch_size or self.config.batch_size
        logger.info(f"Creating test DataLoader with batch size {batch_size}")
        return self._create_loader(self.test_dataset, batch_size, shuffle=shuffle)

    def get_dataset_sizes(self) -> Dict[str, int]:
        sizes = {
            "train": len(self.train_dataset),
            "val": len(self.val_dataset),
            "test": len(self.test_dataset)
        }
        logger.info(f"Dataset sizes: {json.dumps(sizes, indent=2)}")
        return sizes

    def get_data_iterator(self, split='train'):
        if split == 'train':
            return iter(self.get_train_loader())
        elif split == 'val':
            return iter(self.get_val_loader())
        elif split == 'test':
            return iter(self.get_test_loader())
        else:
            raise ValueError(f"Invalid split: {split}")

    def get_sample(self, split='train', num_samples=5) -> List[Dict]:
        loader = self.get_data_iterator(split)
        samples = []
        for i, batch in enumerate(loader):
            if i >= num_samples:
                break
            samples.append(batch)
        logger.info(f"Retrieved {len(samples)} samples from {split} dataset")
        return samples

    def get_vocab_info(self) -> Dict[str, int]:
        vocab_info = {
            "vocab_size": len(self.train_dataset.tokenizer),
            "pad_token_id": self.train_dataset.tokenizer.pad_token_id,
            "eos_token_id": self.train_dataset.tokenizer.eos_token_id,
        }
        logger.info(f"Vocabulary info: {json.dumps(vocab_info, indent=2)}")
        return vocab_info

    def log_dataset_statistics(self):
        for split, dataset in [("train", self.train_dataset),
                               ("val", self.val_dataset),
                               ("test", self.test_dataset)]:
            logger.info(f"{split.capitalize()} dataset statistics:")
            logger.info(f"  - Total samples: {len(dataset)}")
            logger.info(f"  - Languages: {', '.join(dataset.get_languages())}")
            logger.info(
                f"  - Average sequence length: {dataset.get_average_sequence_length():.2f}")


config = Config()
data_loader = MultilingualDataLoader(config)
data_loader.log_dataset_statistics()
