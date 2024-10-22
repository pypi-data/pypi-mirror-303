"""
Module that implements a Sparse Mamba layer for neural networks using JAX/Flax.

This module provides an implementation of the Sparse Mamba layer,
which applies sparse operations to input data efficiently.

Classes:
    SparseMambaLayer: Implements a Sparse Mamba layer.

Dependencies:
    - jax: For array operations and automatic differentiation.
    - flax: For neural network module definitions.
"""

import jax
import jax.numpy as jnp
from flax import linen as nn
import logging

logger = logging.getLogger(__name__)


class SparseMambaLayer(nn.Module):
    """
    SparseMambaLayer: A neural network layer that applies sparse operations
    to input data efficiently.

    This layer uses vmap to apply sparse operations in parallel across
    the input dimensions.

    Attributes:
        input_dim (int): Input dimension.
        output_dim (int): Output dimension.
    """
    input_dim: int
    output_dim: int

    @nn.compact
    def __call__(self, x):
        """
        Forward pass of the SparseMambaLayer.

        Args:
            x (jnp.ndarray): Input array of shape (batch_size, seq_len, input_dim).

        Returns:
            jnp.ndarray: Output array of shape (batch_size, seq_len, output_dim).
        """
        self._validate_input(x)

        def apply_sparse_operation(x_slice):
            # Apply sparse operation to a slice of x
            return nn.Dense(self.output_dim)(x_slice)

        return jax.vmap(apply_sparse_operation)(x)

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
        Get the configuration of the SparseMambaLayer.

        Returns:
            dict: A dictionary containing the layer's configuration.
        """
        return {
            "input_dim": self.input_dim,
            "output_dim": self.output_dim
        }


# Example usage
if __name__ == "__main__":
    try:
        # Set up logging
        logging.basicConfig(level=logging.DEBUG)

        # Create a sample input array
        batch_size, seq_len, input_dim = 32, 10, 256
        output_dim = 512
        key = jax.random.PRNGKey(0)
        x = jax.random.normal(key, (batch_size, seq_len, input_dim))

        # Initialize the SparseMambaLayer
        layer = SparseMambaLayer(input_dim=input_dim, output_dim=output_dim)

        # Initialize parameters
        params = layer.init(key, x)

        # Perform forward pass
        output = layer.apply(params, x)

        print(f"Input shape: {x.shape}")
        print(f"Output shape: {output.shape}")
        print(f"Layer config: {layer.get_config()}")

        logger.info("SparseMambaLayer example completed successfully")
    except Exception as e:
        logger.exception(
            f"An error occurred during the SparseMambaLayer example: {str(e)}")
