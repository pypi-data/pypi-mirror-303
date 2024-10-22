"""
Module that implements a BitNet layer for neural networks using JAX/Flax.

This module provides an implementation of the BitNet layer, which uses
grouped 1D convolutions and a GELU activation to process input arrays.

Classes:
    BitNetLayer: Implements a BitNet layer.

Dependencies:
    - jax: For array operations and automatic differentiation.
    - flax: For neural network module definitions.
"""

import jax
import jax.numpy as jnp
from flax import linen as nn
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BitNetLayer(nn.Module):
    """
    A BitNet layer implementation with 1D convolution and GELU activation.

    This layer applies a 1D convolution followed by GELU activation, with options
    for grouping, dropout, and layer normalization.

    Attributes:
        in_dim (int): Number of input channels.
        out_dim (int): Number of output channels.
        kernel_size (int): Size of the convolving kernel.
        groups (int): Number of groups for grouped convolution.
        dropout_rate (float): Dropout rate for regularization.
        use_layer_norm (bool): Whether to use layer normalization.
    """

    in_dim: int
    out_dim: int
    kernel_size: int = 3
    groups: int = None
    dropout_rate: float = 0.1
    use_layer_norm: bool = True

    @nn.compact
    def __call__(self, x: jnp.ndarray, training: bool = True) -> jnp.ndarray:
        """
        Forward pass of the BitNetLayer.

        Args:
            x (jnp.ndarray): Input array of shape (batch_size, sequence_length, in_dim).
            training (bool): Whether the model is in training mode.

        Returns:
            jnp.ndarray: Output array of shape (batch_size, sequence_length, out_dim).
        """
        logger.debug(f"Starting forward pass with input shape: {x.shape}")
        self._validate_input(x)

        groups = self.groups or self.in_dim
        if self.in_dim % groups != 0 or self.out_dim % groups != 0:
            error_msg = f"Input dimension ({self.in_dim}) and output dimension ({self.out_dim}) " \
                        f"must be divisible by the number of groups ({groups})."
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Transpose input for 1D convolution
        x = jnp.transpose(x, (0, 2, 1))
        logger.debug(f"Transposed input shape: {x.shape}")

        padding = [(self.kernel_size - 1) // 2, (self.kernel_size - 1) // 2]
        x = nn.Conv(features=self.out_dim, kernel_size=(self.kernel_size,),
                    padding=padding, feature_group_count=groups, use_bias=False)(x)
        logger.debug(f"Shape after convolution: {x.shape}")

        x = nn.gelu(x)
        logger.debug("Applied GELU activation")

        x = nn.Dropout(rate=self.dropout_rate, deterministic=not training)(x)
        logger.debug(f"Applied dropout with rate {self.dropout_rate}")

        # Transpose back
        x = jnp.transpose(x, (0, 2, 1))
        logger.debug(f"Final shape after transpose: {x.shape}")

        if self.use_layer_norm:
            x = nn.LayerNorm()(x)
            logger.debug("Applied layer normalization")

        logger.info(f"Completed forward pass. Output shape: {x.shape}")
        return x

    def _validate_input(self, x: jnp.ndarray):
        """Validate the input array dimensions."""
        if x.ndim != 3:
            error_msg = f"Expected input array with 3 dimensions (batch_size, sequence_length, in_dim), " \
                        f"but got {x.ndim} dimensions."
            logger.error(error_msg)
            raise ValueError(error_msg)
        if x.shape[-1] != self.in_dim:
            error_msg = f"Expected number of input channels {self.in_dim}, but got {x.shape[-1]}."
            logger.error(error_msg)
            raise ValueError(error_msg)
        if x.shape[1] < self.kernel_size:
            error_msg = f"Sequence length must be at least {self.kernel_size} " \
                        f"to apply kernel_size={self.kernel_size} convolution."
            logger.error(error_msg)
            raise ValueError(error_msg)
        logger.debug("Input validation passed")

    def get_config(self) -> dict:
        """
        Get the configuration of the BitNetLayer.

        Returns:
            dict: A dictionary containing the layer's configuration.
        """
        config = {
            "in_dim": self.in_dim,
            "out_dim": self.out_dim,
            "kernel_size": self.kernel_size,
            "groups": self.groups,
            "dropout_rate": self.dropout_rate,
            "use_layer_norm": self.use_layer_norm
        }
        logger.info(f"Retrieved layer configuration: {config}")
        return config

# Example usage
if __name__ == "__main__":
    try:
        logger.info("Starting BitNetLayer example")

        # Create a sample input array
        batch_size, in_dim, sequence_length = 32, 64, 128
        x = jax.random.normal(jax.random.PRNGKey(0), (batch_size, sequence_length, in_dim))
        logger.info(f"Created sample input with shape: {x.shape}")

        # Initialize the BitNetLayer
        layer = BitNetLayer(in_dim=64, out_dim=128, kernel_size=3, groups=16, dropout_rate=0.1, use_layer_norm=True)
        logger.info("Initialized BitNetLayer")

        # Initialize parameters
        params = layer.init(jax.random.PRNGKey(1), x)
        logger.info("Initialized layer parameters")

        # Perform forward pass
        output = layer.apply(params, x)
        logger.info(f"Performed forward pass. Output shape: {output.shape}")

        print(f"Input shape: {x.shape}")
        print(f"Output shape: {output.shape}")
        print(f"Layer config: {layer.get_config()}")

        logger.info("BitNetLayer example completed successfully")
    except Exception as e:
        logger.exception(f"An error occurred during the BitNetLayer example: {str(e)}")
