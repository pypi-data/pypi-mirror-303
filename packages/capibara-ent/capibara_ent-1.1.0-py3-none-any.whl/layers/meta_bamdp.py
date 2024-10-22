"""
Module that implements a Meta BAMDP layer for neural networks using JAX/Flax.

This module provides an implementation of the Meta BAMDP layer,
which applies a meta-learning operation to input data efficiently.

Classes:
    MetaBAMDPLayer: Implements a Meta BAMDP layer.

Dependencies:
    - jax: For array operations and automatic differentiation.
    - flax: For neural network module definitions.
"""

import jax
import jax.numpy as jnp
from flax import linen as nn
import logging

logger = logging.getLogger(__name__)


class MetaBAMDPLayer(nn.Module):
    """
    MetaBAMDPLayer: A neural network layer that applies a meta-learning operation
    to input data efficiently.

    This layer uses vmap to apply the meta operation in parallel across
    the input dimensions.

    Attributes:
        input_dim (int): Input dimension.
        hidden_dim (int): Hidden state dimension.
        output_dim (int): Output dimension.
    """
    input_dim: int
    hidden_dim: int
    output_dim: int

    @nn.compact
    def __call__(self, x, training=True):
        """
        Forward pass of the MetaBAMDPLayer.

        Args:
            x (jnp.ndarray): Input array of shape (batch_size, seq_len, input_dim).
            training (bool): Whether the model is in training mode.

        Returns:
            jnp.ndarray: Output array of shape (batch_size, seq_len, output_dim).
        """
        self._validate_input(x)

        def meta_operation(x_slice):
            h = nn.Dense(self.hidden_dim)(x_slice)
            h = jax.nn.relu(h)
            h = nn.Dropout(rate=0.1)(h, deterministic=not training)
            return nn.Dense(self.output_dim)(h)

        return jax.vmap(meta_operation)(x)

    def _validate_input(self, x: jnp.ndarray):
        """Validate the input array dimensions."""
        if x.ndim != 3:
            error_msg = f"Expected input array with 3 dimensions (batch_size, seq_len, input_dim), but got {
                x.ndim} dimensions."
            logger.error(error_msg)
            raise ValueError(error_msg)
        if x.shape[-1] != self.input_dim:
            error_msg = f"Expected input_dim to be {
                self.input_dim}, but got {x.shape[-1]}."
            logger.error(error_msg)
            raise ValueError(error_msg)

    def get_config(self) -> dict:
        """
        Get the configuration of the MetaBAMDPLayer.

        Returns:
            dict: A dictionary containing the layer's configuration.
        """
        return {
            "input_dim": self.input_dim,
            "hidden_dim": self.hidden_dim,
            "output_dim": self.output_dim
        }


# Example usage
if __name__ == "__main__":
    try:
        # Set up logging
        logging.basicConfig(level=logging.DEBUG)

        # Create a sample input array
        batch_size, seq_len, input_dim = 32, 10, 256
        hidden_dim = 512
        output_dim = 256
        key = jax.random.PRNGKey(0)
        x = jax.random.normal(key, (batch_size, seq_len, input_dim))

        # Initialize the MetaBAMDPLayer
        layer = MetaBAMDPLayer(input_dim=input_dim,
                               hidden_dim=hidden_dim, output_dim=output_dim)

        # Initialize parameters
        params = layer.init(key, x, training=True)

        # Perform forward pass
        output = layer.apply(params, x, training=True)

        print(f"Input shape: {x.shape}")
        print(f"Output shape: {output.shape}")
        print(f"Layer config: {layer.get_config()}")

        logger.info("MetaBAMDPLayer example completed successfully")
    except Exception as e:
        logger.exception(
            f"An error occurred during the MetaBAMDPLayer example: {str(e)}")
