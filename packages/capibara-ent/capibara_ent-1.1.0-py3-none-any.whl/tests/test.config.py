# tests/__init__.py

from capibara.config import CapibaraConfig
import jax
import jax.numpy as jnp
import pytest
from typing import Dict, Any

__all__ = ['create_test_model', 'TEST_CONFIG', 'initialize_tests']

DEFAULT_CONFIG: Dict[str, Any] = {
    'd_model': 512,
    'd_state': 256,
    'd_conv': 128,
    'expand': 2,
    'base_model_name': 'gpt2',
    'translation_model': 'facebook/m2m100_418M',
    'get_active_layers': lambda: ['platonic', 'game_theory', 'ethics'],
    'get_layer_config': lambda layer_name: {},
    'personality': {},
    'context_window_size': 10,
    'max_length': 50,
    'vocab_size': 1000
}

# `TEST_CONFIG` defines the common configuration for model testing.
TEST_CONFIG = CapibaraConfig(**DEFAULT_CONFIG)


def create_test_model(overrides: Dict[str, Any] = None):
    """
    Creates a CapibaraENT model using the test configuration, allowing for optional overrides.

    Args:
        overrides (dict, optional): Dictionary with configuration fields to override.

    Returns:
        CapibaraENT: A text generator model instance initialized with 
        the TEST_CONFIG settings or overridden settings.
    """
    from capibara.models.model import CapibaraENT

    config_dict = DEFAULT_CONFIG.copy()
    if overrides:
        config_dict.update(overrides)
    config = CapibaraConfig(**config_dict)
    return CapibaraENT(config)


@pytest.fixture
def capibara_test_model():
    """
    Pytest fixture that returns a CapibaraENT model instance for testing.

    Returns:
        CapibaraENT: A text generator model instance initialized with TEST_CONFIG settings.
    """
    return create_test_model()


def create_random_input(key, batch_size=1, seq_len=None):
    """
    Creates random input for testing.

    Args:
        key (jax.random.PRNGKey): A PRNG key used as the random key.
        batch_size (int): The batch size of the input.
        seq_len (int, optional): The sequence length. If None, uses TEST_CONFIG.max_length.

    Returns:
        jnp.ndarray: Random input ids.
    """
    if seq_len is None:
        seq_len = TEST_CONFIG.max_length
    return jax.random.randint(key, (batch_size, seq_len), 0, TEST_CONFIG.vocab_size)


def initialize_tests():
    """
    This function can be used for initializing any setup required for running all tests.
    This might include setting up random seeds, etc.
    """
    # Set a fixed random seed for reproducibility in tests
    jax.random.PRNGKey(42)

    # Additional initialization steps can be added here as needed


if __name__ == '__main__':
    initialize_tests()
