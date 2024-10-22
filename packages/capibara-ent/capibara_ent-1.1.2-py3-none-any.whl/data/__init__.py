"""
Data package for CapibaraGPT.

This package provides utilities for handling multilingual datasets,
including data loading, preprocessing, and augmentation.

Modules:
    dataset: Provides MultilingualDataset and DataLoader classes.
    preprocessing: Contains functions for text preprocessing.
    augmentation: Offers data augmentation techniques.

Classes:
    MultilingualDataset: Handles multilingual text datasets.
    DataLoader: Manages data loading for training and evaluation.

Functions:
    preprocess_text: Preprocesses text data for model input.
    augment_data: Applies data augmentation techniques.

Version:
    0.1.0
"""

from .dataset import MultilingualDataset, DataLoader
from .preprocessing import preprocess_text
from .augmentation import augment_data

__all__ = ['MultilingualDataset', 'DataLoader',
           'preprocess_text', 'augment_data']

__version__ = '0.1.0'

# Opcional: Configuración de logging para el paquete
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

# Opcional: Verificación de dependencias
try:
    import torch
    import transformers
except ImportError as e:
    logger.warning(f"Required dependency not found: {e}")

# Opcional: Inicialización del paquete


def initialize():
    """Initialize the data package."""
    logger.info("Initializing CapibaraGPT data package...")
    # Aquí puedes añadir cualquier lógica de inicialización necesaria
    logger.info("CapibaraGPT data package initialized successfully.")


initialize()
