"""
Test module for the CapibaraENT data loader and model.

This module contains unit tests for the CapibaraDataset, data loading functions,
and model operations using JAX and Flax.

Classes:
    TestCapibaraJAX: Test class for the data loader and model.

Dependencies:
    - unittest: For creating and running unit tests.
    - jax: For array operations and gradients.
    - flax: For neural network layers and model definition.
    - capibara: For the classes and functions being tested.
"""

import unittest
import jax
import jax.numpy as jnp
from jax import random
from flax import linen as nn
from flax.training import train_state
import optax

from capibara.config import CapibaraConfig
from capibara.models.model import CapibaraENT
from capibara.data import CapibaraDataset, CapibaraDataLoader


class TestCapibaraJAX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment for all test methods in the class.
        This method is called once before any test method is run.
        """
        # Set a fixed random seed for reproducibility
        cls.rng = random.PRNGKey(42)

    def setUp(self):
        """
        Sets up the test environment for each test method.

        Initializes the configuration and creates mock data for testing.
        """
        self.config = CapibaraConfig(
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
            max_length=100,
            vocab_size=1000,
            batch_size=32
        )
        self.mock_data = self.generate_mock_data(
            num_samples=100, sequence_length=50)

    def generate_mock_data(self, num_samples, sequence_length):
        """
        Generates mock data for testing.

        Args:
            num_samples (int): Number of mock samples to generate.
            sequence_length (int): Length of each sequence.

        Returns:
            list: A list of dictionaries containing 'text' data for testing.
        """
        return [{'text': 'Sample text ' * sequence_length} for _ in range(num_samples)]

    def test_data_loader_creation(self):
        """
        Tests the creation of the CapibaraDataLoader.
        """
        dataset = CapibaraDataset(self.mock_data, self.config)
        dataloader = CapibaraDataLoader(dataset, self.config)

        batches = [next(iter(dataloader))
                   for _ in range(3)]  # Only check the first 3 batches

        self.assertEqual(len(batches), 3)
        for batch in batches:
            self.assertEqual(
                batch.shape, (self.config.batch_size, self.config.max_length))

    def test_model_creation(self):
        """
        Tests the creation of the CapibaraENT model.
        """
        model = CapibaraENT(self.config)
        self.assertIsInstance(model, CapibaraENT)

    def test_forward_pass(self):
        """
        Tests a forward pass through the model.
        """
        model = CapibaraENT(self.config)
        rng, input_rng = random.split(self.rng)
        input_data = random.randint(
            input_rng, (self.config.batch_size, self.config.max_length), 0, self.config.vocab_size)

        params = model.init(rng, input_data)
        output = model.apply(params, input_data)

        self.assertIn('output', output)
        self.assertEqual(output['output'].shape, (self.config.batch_size,
                         self.config.max_length, self.config.vocab_size))

    def test_gradient_computation(self):
        """
        Tests gradient computation.

        This test ensures that the gradients are being computed correctly
        for a simple forward and backward pass using the model.
        """
        model = CapibaraENT(self.config)
        rng, input_rng, params_rng = random.split(self.rng, 3)

        input_data = random.randint(
            input_rng, (self.config.batch_size, self.config.max_length), 0, self.config.vocab_size)
        labels = random.randint(
            input_rng, (self.config.batch_size,), 0, self.config.vocab_size)

        params = model.init(params_rng, input_data)

        def loss_fn(params):
            logits = model.apply(params, input_data)['output']
            one_hot = jax.nn.one_hot(labels, self.config.vocab_size)
            loss = jnp.mean(optax.softmax_cross_entropy(logits, one_hot))
            return loss

        grad_fn = jax.grad(loss_fn)
        grads = grad_fn(params)

        # Check that gradients exist and are not NaN
        for name, param_grads in grads.items():
            self.assertIsNotNone(param_grads, f"Gradient for {name} is None")
            self.assertFalse(jnp.isnan(param_grads).any(),
                             f"NaN gradient for {name}")


if __name__ == '__main__':
    unittest.main()
