"""
Module that implements a Liquid layer for neural networks using JAX/Flax.

This module provides an implementation of the Liquid layer, which utilizes
linear transformations, GELU activation, and layer normalization
to process input arrays.

Classes:
    LiquidLayer: Implements a Liquid layer.

Dependencies:
    - jax: For array operations and automatic differentiation.
    - flax: For neural network module definitions.
"""

import jax
import jax.numpy as jnp
from flax import linen as nn
from pydantic import validator
import logging

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class LiquidLayer(nn.Module):
    """
    LiquidLayer: A flexible and efficient neural network layer.

    This layer implements a linear transformation followed by GELU activation,
    with options for normalization, dropout, and residual connections.

    Attributes:
        dim (int): Input and output dimension.
        expansion_factor (int): Expansion factor for the hidden layer.
        dropout_rate (float): Dropout rate for regularization.
        use_expansion (bool): Whether to use dimension expansion.
    """

    dim: int
    expansion_factor: int = 4
    dropout_rate: float = 0.1
    use_expansion: bool = True

    @validator('expansion_factor')
    def check_expansion_factor(cls, v):
        if v < 1:
            error_msg = "expansion_factor must be at least 1."
            logger.error(error_msg)
            raise ValueError(error_msg)
        return v

    @validator('dropout_rate')
    def check_dropout_rate(cls, v):
        if not 0.0 <= v < 1.0:
            error_msg = "dropout_rate must be in the range [0.0, 1.0)."
            logger.error(error_msg)
            raise ValueError(error_msg)
        return v

    @nn.compact
    def __call__(self, x: jnp.ndarray, training: bool = True) -> jnp.ndarray:
        """
        Forward pass of the LiquidLayer.

        Args:
            x (jnp.ndarray): Input array of shape (batch_size, sequence_length, dim).
            training (bool): Whether the model is in training mode.

        Returns:
            jnp.ndarray: Output array of shape (batch_size, sequence_length, dim).
        """
        self._validate_input(x)
        logger.debug(f"Input shape: {x.shape}")

        residual = x
        if self.use_expansion:
            logger.debug("Using dimension expansion")
            expanded = nn.Dense(features=self.dim *
                                self.expansion_factor, use_bias=False)(x)
            logger.debug(f"Expanded shape: {expanded.shape}")
            activated = nn.gelu(expanded, approximate=True)
            logger.debug(f"Activated shape: {activated.shape}")
            dropped = nn.Dropout(rate=self.dropout_rate,
                                 deterministic=not training)(activated)
            logger.debug(f"Dropped shape: {dropped.shape}")
            projected = nn.Dense(features=self.dim, use_bias=False)(dropped)
            logger.debug(f"Projected shape: {projected.shape}")
        else:
            logger.debug("Skipping dimension expansion")
            projected = x

        normalized = nn.LayerNorm()(projected)
        logger.debug(f"Normalized shape: {normalized.shape}")
        output = normalized + residual
        logger.debug(f"Output shape: {output.shape}")

        return output

    def _validate_input(self, x: jnp.ndarray):
        """Validate the input array dimensions."""
        if x.ndim != 3:
            logger.warning(
                f"Input has {x.ndim} dimensions, expected 3. Proceeding with potential issues.")
        if x.shape[-1] != self.dim:
            logger.warning(f"Expected input dimension to be {
                           self.dim}, but got {x.shape[-1]}.")

    def get_config(self) -> dict:
        """
        Get the configuration of the LiquidLayer.

        Returns:
            dict: A dictionary containing the layer's configuration.
        """
        config = {
            "dim": self.dim,
            "expansion_factor": self.expansion_factor,
            "dropout_rate": self.dropout_rate,
            "use_expansion": self.use_expansion
        }
        logger.debug(f"Layer config: {config}")
        return config


# Example usage
if __name__ == "__main__":
    try:
        logger.info("Starting LiquidLayer example")

        # Create a sample input array
        batch_size, sequence_length, dim = 32, 128, 256
        x = jax.random.normal(jax.random.PRNGKey(
            0), (batch_size, sequence_length, dim))
        logger.info(f"Created sample input array with shape {x.shape}")

        # Initialize the LiquidLayer
        layer = LiquidLayer(dim=256, expansion_factor=4,
                            dropout_rate=0.1, use_expansion=True)
        logger.info("Initialized LiquidLayer")

        # Initialize parameters
        params = layer.init(jax.random.PRNGKey(1), x)
        logger.info("Initialized layer parameters")

        # Perform forward pass
        output = layer.apply(params, x)
        logger.info(f"Performed forward pass. Output shape: {output.shape}")

        print(f"Input shape: {x.shape}")
        print(f"Output shape: {output.shape}")
        print(f"Layer config: {layer.get_config()}")

        logger.info("LiquidLayer example completed successfully")
    except Exception as e:
        logger.exception(
            f"An error occurred during the LiquidLayer example: {str(e)}")
