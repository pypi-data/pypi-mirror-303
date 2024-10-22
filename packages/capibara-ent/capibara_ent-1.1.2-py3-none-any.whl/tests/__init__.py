# This file is intentionally empty to mark the directory as a Python package.
# It allows the test modules to be imported correctly.

# Common imports for all tests
import jax
import jax.numpy as jnp
import pytest
from capibara_model.config import CapibaraConfig
from capibara_model.model import CapibaraTextGenerator

# Common configuration for tests
TEST_CONFIG = CapibaraConfig(
    input_dim=64,
    byte_output_dim=128,
    state_dim=256,
    mamba_output_dim=512,
    hidden_dim=1024,
    output_dim=2048,
    vocab_size=1000,
    max_length=50,
    num_layers=4
)

# Utility functions for tests


def create_test_model() -> CapibaraTextGenerator:
    """
    Creates a CapibaraTextGenerator model using the test configuration.

    This function provides a utility to create a model with the predefined
    configuration that is commonly used in testing. By centralizing the model 
    creation, tests can ensure they are using a consistent configuration across
    different test cases.

    Returns:
        CapibaraTextGenerator: A text generator model instance initialized with 
        the TEST_CONFIG settings.
    """
    return CapibaraTextGenerator(TEST_CONFIG)


def create_random_input(key: jax.random.PRNGKey, batch_size: int = 1) -> jnp.ndarray:
    """
    Creates a random input array for testing.

    Args:
        key (jax.random.PRNGKey): A PRNG key used as the random key.
        batch_size (int): The batch size for the input array. Defaults to 1.

    Returns:
        jnp.ndarray: A random integer array of shape (batch_size, max_length)
        with values in the range [0, vocab_size).
    """
    return jax.random.randint(key, (batch_size, TEST_CONFIG.max_length), 0, TEST_CONFIG.vocab_size)

# Pytest fixtures


@pytest.fixture
def capibara_model():
    """
    Pytest fixture that provides a CapibaraTextGenerator model for testing.

    This fixture can be used in test functions to get a fresh model instance
    for each test, ensuring test isolation.

    Returns:
        CapibaraTextGenerator: A text generator model instance.
    """
    return create_test_model()


@pytest.fixture
def rng_key():
    """
    Pytest fixture that provides a JAX random key for testing.

    This fixture can be used in test functions to get a fresh random key
    for each test, ensuring reproducibility and test isolation.

    Returns:
        jax.random.PRNGKey: A JAX PRNG key.
    """
    return jax.random.PRNGKey(0)


SMALL_TEST_CONFIG = CapibaraConfig(...)
LARGE_TEST_CONFIG = CapibaraConfig(...)
