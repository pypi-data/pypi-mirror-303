"""
Module that implements a Mamba Byte layer for neural networks using JAX/Flax.

This module provides an implementation of the Mamba Byte layer,
which combines Mamba SSM with other advanced techniques like BitNet, Liquid layers,
and sparse Mamba for efficient processing of byte-level inputs.

Classes:
    MambaByteLayer: Implements a Mamba Byte layer.

Dependencies:
    - jax: For array operations and automatic differentiation.
    - flax: For neural network module definitions.
"""

import jax
import jax.numpy as jnp
from flax import linen as nn
import logging

from .synthetic_embedding import SyntheticEmbeddingLayer
from .bitnet import BitNetLayer
from .liquid import LiquidLayer
from .sparse_mamba import SparseMambaLayer
from .bitnet_quantizer import BitNetQuantizer
from .meta_bamdp import MetaBAMDPLayer
from .mamba_ssm import MambaSSMLayer

logger = logging.getLogger(__name__)


class MambaByteLayer(nn.Module):
    """
    MambaByteLayer: An advanced neural network layer combining various techniques
    for efficient processing of byte-level inputs.

    This layer implements a sequence of operations including Mamba SSM,
    synthetic embedding, BitNet, Liquid layers, sparse Mamba, and quantization.

    Attributes:
        dim (int): Input and output dimension.
        num_bitnet_layers (int): Number of BitNet layers.
        num_liquid_layers (int): Number of Liquid layers.
        dropout_rate (float): Dropout rate for regularization.
        use_residual (bool): Whether to use residual connections.
    """
    dim: int
    num_bitnet_layers: int
    num_liquid_layers: int
    dropout_rate: float = 0.1
    use_residual: bool = True

    def setup(self):
        self.mamba_byte = MambaSSMLayer(self.dim)
        self.synthetic_embedding = SyntheticEmbeddingLayer(self.dim)
        self.bitnet_layers = [BitNetLayer()
                              for _ in range(self.num_bitnet_layers)]
        self.liquid_layers = [LiquidLayer()
                              for _ in range(self.num_liquid_layers)]
        self.sparse_mamba = SparseMambaLayer()
        self.mamba2 = MambaSSMLayer(self.dim)
        self.bitnet_quantizer = BitNetQuantizer()
        self.meta_bamdp = MetaBAMDPLayer()
        self.final_fc = nn.Dense(features=self.dim)

    def __call__(self, x, training=True):
        """
        Forward pass of the MambaByteLayer.

        Args:
            x (jnp.ndarray): Input array of shape (batch_size, seq_len, dim).
            training (bool): Whether the model is in training mode.

        Returns:
            jnp.ndarray: Output array of shape (batch_size, seq_len, dim).
        """
        self._validate_input(x)

        # Apply mamba_byte and synthetic_embedding
        x = self.mamba_byte(x)
        x = self.synthetic_embedding(x, training=training)

        if self.use_residual:
            residual = x

        # Define a function to apply a bitnet and liquid layer
        def apply_bitnet_liquid(bitnet, liquid, x):
            x = jnp.transpose(bitnet(jnp.transpose(x, (0, 2, 1))), (0, 2, 1))
            return liquid(x)

        # Use vmap to apply the layers in parallel
        x = jax.vmap(apply_bitnet_liquid, in_axes=(0, 0, None))(
            jnp.array(self.bitnet_layers),
            jnp.array(self.liquid_layers),
            x
        )

        # Continue with the rest of the processing
        x = self.sparse_mamba(x)
        x = self.mamba2(x)
        x = self.bitnet_quantizer(x)
        x = self.meta_bamdp(x)
        x = self.final_fc(x)

        if self.use_residual:
            x = x + residual

        x = nn.Dropout(rate=self.dropout_rate)(x, deterministic=not training)

        return x

    def _validate_input(self, x: jnp.ndarray):
        """Validate the input array dimensions."""
        if x.ndim != 3:
            error_msg = f"Expected input array with 3 dimensions (batch_size, seq_len, dim), but got {
                x.ndim} dimensions."
            logger.error(error_msg)
            raise ValueError(error_msg)
        if x.shape[-1] != self.dim:
            error_msg = f"Expected dim to be {
                self.dim}, but got {x.shape[-1]}."
            logger.error(error_msg)
            raise ValueError(error_msg)

    def get_config(self) -> dict:
        """
        Get the configuration of the MambaByteLayer.

        Returns:
            dict: A dictionary containing the layer's configuration.
        """
        return {
            "dim": self.dim,
            "num_bitnet_layers": self.num_bitnet_layers,
            "num_liquid_layers": self.num_liquid_layers,
            "dropout_rate": self.dropout_rate,
            "use_residual": self.use_residual
        }


# Example usage
if __name__ == "__main__":
    try:
        # Set up logging
        logging.basicConfig(level=logging.DEBUG)

        # Create a sample input array
        batch_size, seq_len, dim = 32, 10, 256
        key = jax.random.PRNGKey(0)
        x = jax.random.normal(key, (batch_size, seq_len, dim))

        # Initialize the MambaByteLayer
        layer = MambaByteLayer(
            dim=256,
            num_bitnet_layers=3,
            num_liquid_layers=3,
            dropout_rate=0.1,
            use_residual=True
        )

        # Initialize parameters
        params = layer.init(key, x, training=True)

        # Perform forward pass
        output = layer.apply(params, x, training=True)

        print(f"Input shape: {x.shape}")
        print(f"Output shape: {output.shape}")
        print(f"Layer config: {layer.get_config()}")

        logger.info("MambaByteLayer example completed successfully")
    except Exception as e:
        logger.exception(
            f"An error occurred during the MambaByteLayer example: {str(e)}")
