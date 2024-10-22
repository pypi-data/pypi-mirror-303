"""
Module for handling multilingual datasets for the CapibaraGPT model.

This module provides a class for creating and managing multilingual
datasets, including language detection and translation of
unsupported texts.

Classes:
    MultilingualDataset: Manages a multilingual dataset.

Dependencies:
    - jax: For array manipulation and model compatibility.
    - transformers: For the AutoTokenizer.
    - langdetect: For language detection.
    - googletrans: For text translation.
    - dotenv: For loading environment variables.
"""

import logging
import os
import json
import jax.numpy as jnp
from typing import List, Dict, Any, Optional, Tuple
from transformers import AutoTokenizer
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor
from langdetect import detect
from googletrans import Translator
from dotenv import load_dotenv
import pickle

logger = logging.getLogger(__name__)


class MultilingualDataset:
    """
    A dataset class for handling multilingual text data.

    This class processes and prepares multilingual text data for use in language models,
    including language detection, translation, and tokenization.

    Attributes:
        data (List[Dict[str, Any]]): List of data items, each containing at least a 'text' field.
        supported_languages (List[str]): List of supported language codes.
        tokenizer: Tokenizer for encoding the text.
        max_length (int): Maximum length for tokenization.
        translation_cache (Dict[int, tuple]): Cache for storing translated texts.
    """

    @classmethod
    def from_directory(cls, directory: str, supported_languages: List[str], **kwargs):
        """
        Create a MultilingualDataset from a directory of JSON files.

        Args:
            directory (str): Path to the directory containing JSON files.
            supported_languages (List[str]): List of supported language codes.
            **kwargs: Additional arguments to pass to the MultilingualDataset constructor.

        Returns:
            MultilingualDataset: A new instance of MultilingualDataset.
        """
        def load_file(filename: str) -> List[Dict[str, Any]]:
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                return json.load(f)

        data = []
        for filename in [f for f in os.listdir(directory) if f.endswith('.json')]:
            data.extend(load_file(filename))

        return cls(data, supported_languages, **kwargs)

    def __init__(self, data: List[Dict[str, Any]], supported_languages: List[str],
                 tokenizer: Optional[Any] = None, max_length: Optional[int] = None):
        """
        Initialize the MultilingualDataset.

        Args:
            data (List[Dict[str, Any]]): List of data items.
            supported_languages (List[str]): List of supported language codes.
            tokenizer (Optional[Any]): Pre-initialized tokenizer. If None, a default one will be used.
            max_length (Optional[int]): Maximum length for tokenization. If None, it will be set to 512.

        Raises:
            ValueError: If data is empty or not in the correct format.
            KeyError: If any data item is missing the 'text' field.
        """
        load_dotenv()
        self.max_length = max_length or int(
            os.getenv('CAPIBARA_MAX_LENGTH', 512))
        self._validate_input(data)
        self.data = data
        self.supported_languages = supported_languages
        self.tokenizer = tokenizer or AutoTokenizer.from_pretrained(
            "xlm-roberta-base")
        self.translation_cache = {}
        self.translator = Translator()

        logger.info(f"Created MultilingualDataset with {len(data)} items.")

    def _validate_input(self, data: List[Dict[str, Any]]) -> None:
        """Validate the input data."""
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("Data must be a non-empty list of dictionaries.")
        if not all(isinstance(item, dict) and 'text' in item for item in data):
            raise ValueError(
                "All items in data must be dictionaries with a 'text' key.")

    def __len__(self) -> int:
        """Return the number of items in the dataset."""
        return len(self.data)

    @lru_cache(maxsize=1000)
    def _detect_and_translate(self, idx: int) -> Tuple[str, str]:
        """Detect language and translate if necessary, with caching."""
        item = self.data[idx]
        text = item['text']
        lang = self._detect_language(text)

        if lang not in self.supported_languages:
            try:
                text = self._translate_text(text, self.supported_languages[0])
                lang = self.supported_languages[0]
                logger.info(f"Translated item {idx} to {
                            self.supported_languages[0]}")
            except Exception as e:
                logger.error(f"Error translating text at index {idx}: {e}")
                lang = self.supported_languages[0]

        return text, lang

    def __getitem__(self, idx: int) -> Dict[str, Any]:
        """
        Get a single item from the dataset.

        Args:
            idx (int): Index of the item to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing 'input_ids', 'attention_mask', and 'lang'.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not 0 <= idx < len(self.data):
            raise IndexError(f"Index {idx} is out of bounds for dataset of length {
                             len(self.data)}.")

        text, lang = self._detect_and_translate(idx)
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='jax'
        )

        return {
            'input_ids': encoding['input_ids'][0],
            'attention_mask': encoding['attention_mask'][0],
            'lang': self.supported_languages.index(lang)
        }

    @staticmethod
    def _detect_language(text: str) -> str:
        """Detect the language of the given text."""
        try:
            return detect(text)
        except:
            return "en"  # default to English if detection fails

    def _translate_text(self, text: str, target_lang: str) -> str:
        """Translate the given text to the target language."""
        try:
            return self.translator.translate(text, dest=target_lang).text
        except:
            return text  # return original text if translation fails

    def get_language_distribution(self) -> Dict[str, int]:
        """Get the distribution of languages in the dataset."""
        lang_dist = {}
        for idx in range(len(self)):
            _, lang = self._detect_and_translate(idx)
            lang_dist[lang] = lang_dist.get(lang, 0) + 1
        return lang_dist

    def save_translation_cache(self, filepath: str) -> None:
        """Save the translation cache to a file."""
        with open(filepath, 'wb') as f:
            pickle.dump(self.translation_cache, f)

    def load_translation_cache(self, filepath: str) -> None:
        """Load the translation cache from a file."""
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                self.translation_cache = pickle.load(f)

    def split_dataset(self, train_ratio: float = 0.8, val_ratio: float = 0.1) -> Tuple['MultilingualDataset', 'MultilingualDataset', 'MultilingualDataset']:
        """
        Split the dataset into train, validation, and test sets.

        Args:
            train_ratio (float): Ratio of data to use for training.
            val_ratio (float): Ratio of data to use for validation.

        Returns:
            Tuple[MultilingualDataset, MultilingualDataset, MultilingualDataset]: Train, validation, and test datasets.
        """
        total = len(self)
        train_size = int(total * train_ratio)
        val_size = int(total * val_ratio)
        test_size = total - train_size - val_size

        train_data = self.data[:train_size]
        val_data = self.data[train_size:train_size+val_size]
        test_data = self.data[train_size+val_size:]

        return (
            MultilingualDataset(
                train_data, self.supported_languages, self.tokenizer, self.max_length),
            MultilingualDataset(
                val_data, self.supported_languages, self.tokenizer, self.max_length),
            MultilingualDataset(
                test_data, self.supported_languages, self.tokenizer, self.max_length)
        )


# Example usage
if __name__ == "__main__":
    sample_data = [
        {"text": "Hello, world!"},
        {"text": "Bonjour le monde!"},
        {"text": "¡Hola mundo!"}
    ]
    supported_langs = ["en", "fr", "es"]

    dataset = MultilingualDataset(sample_data, supported_langs)
    print(f"Dataset size: {len(dataset)}")
    print(f"First item: {dataset[0]}")
    print(f"Language distribution: {dataset.get_language_distribution()}")
