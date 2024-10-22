"""
Module that implements a Mamba2 layer for neural networks using JAX/Flax.

This module provides an implementation of the Mamba2 layer,
which applies a recurrent operation to input data efficiently.

Classes:
    Mamba2Layer: Implements a Mamba2 layer.

Dependencies:
    - jax: For array operations and automatic differentiation.
    - flax: For neural network module definitions.
"""

import jax
import jax.numpy as jnp
from flax import linen as nn
import logging

logger = logging.getLogger(__name__)


class Mamba2Layer(nn.Module):
    """
    Mamba2Layer: A neural network layer that applies a recurrent operation
    to input data efficiently.

    This layer uses jax.lax.scan to apply the Mamba2 operation across
    the time dimension of the input.

    Attributes:
        input_dim (int): Input dimension.
        hidden_dim (int): Hidden state dimension.
        output_dim (int): Output dimension.
    """
    input_dim: int
    hidden_dim: int
    output_dim: int

    @nn.compact
    def __call__(self, x):
        """
        Forward pass of the Mamba2Layer.

        Args:
            x (jnp.ndarray): Input array of shape (batch_size, seq_len, input_dim).

        Returns:
            jnp.ndarray: Output array of shape (batch_size, seq_len, output_dim).
        """
        self._validate_input(x)

        def mamba_step(carry, x_t):
            h = carry
            h = nn.Dense(self.hidden_dim)(jnp.concatenate([x_t, h]))
            h = jax.nn.gelu(h)
            output = nn.Dense(self.output_dim)(h)
            return h, output

        init_state = jnp.zeros((x.shape[0], self.hidden_dim))
        _, outputs = jax.lax.scan(mamba_step, init_state, x.transpose(1, 0, 2))
        return outputs.transpose(1, 0, 2)

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
        Get the configuration of the Mamba2Layer.

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

        # Initialize the Mamba2Layer
        layer = Mamba2Layer(input_dim=input_dim,
                            hidden_dim=hidden_dim, output_dim=output_dim)

        # Initialize parameters
        params = layer.init(key, x)

        # Perform forward pass
        output = layer.apply(params, x)

        print(f"Input shape: {x.shape}")
        print(f"Output shape: {output.shape}")
        print(f"Layer config: {layer.get_config()}")

        logger.info("Mamba2Layer example completed successfully")
    except Exception as e:
        logger.exception(
            f"An error occurred during the Mamba2Layer example: {str(e)}")
