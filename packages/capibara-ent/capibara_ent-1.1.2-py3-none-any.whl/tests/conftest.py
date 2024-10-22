# tests/conftest.py

import pytest
import jax
import jax.numpy as jnp
from jax import random
import os
from capibara.config import CapibaraConfig
from capibara.models.model import CapibaraENT


def initialize_tests():
    """
    Initialize the necessary configuration for running all tests.
    This includes setting up random seeds, environment variables, and other configurations.
    """
    # Set a fixed random seed for reproducibility in tests
    jax.random.PRNGKey(42)

    # Configure JAX backend if necessary
    # For example, to use CPU, GPU or TPU
    # jax.config.update('jax_platform_name', 'cpu')

    # Set logging level for tests
    os.environ['CAPIBARA_LOG_LEVEL'] = 'ERROR'

    # Add other necessary configurations here


@pytest.fixture(scope="session", autouse=True)
def setup_tests():
    """
    Fixture that runs once at the beginning of the test session.
    """
    initialize_tests()
    yield  # This allows the tests to run
    # Perform any necessary cleanup after all tests


@pytest.fixture
def test_config():
    """
    Fixture that provides a test configuration for the CapibaraENT model.
    """
    return CapibaraConfig(
        d_model=512,
        d_state=256,
        d_conv=128,
        expand=2,
        base_model_name='gpt2',
        translation_model='facebook/m2m100_418M',
        get_active_layers=lambda: ['platonic', 'game_theory', 'ethics'],
        get_layer_config=lambda layer_name: {},
        personality={},
        context_window_size=10,
        max_length=50,
        vocab_size=1000
    )


@pytest.fixture
def capibara_model(test_config):
    """
    Fixture that provides an instance of the CapibaraENT model for testing.
    """
    return CapibaraENT(test_config)


@pytest.fixture
def rng_key():
    """
    Fixture that provides a PRNG key for generating random numbers.
    """
    return jax.random.PRNGKey(0)


@pytest.fixture
def sample_input(rng_key, test_config):
    """
    Fixture that provides a sample input for the model.
    """
    return jax.random.randint(rng_key, (1, test_config.max_length), 0, test_config.vocab_size)


@pytest.fixture
def model_params(capibara_model, sample_input):
    """
    Fixture that provides the initialized parameters of the model.
    """
    return capibara_model.init(rng_key, sample_input)['params']


def test_model_forward(capibara_model, sample_input, model_params):
    output = capibara_model.apply({'params': model_params}, sample_input)
    assert output['output'].shape == (
        1, test_config.max_length, test_config.vocab_size)
