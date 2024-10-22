"""
Module that implements a Self-Attention layer for neural networks using JAX/Flax.

This module provides an implementation of the Self-Attention layer,
which uses multi-head attention and layer normalization to process
input arrays.

Classes:
    SelfAttentionLayer: Implements a Self-Attention layer.

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
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SelfAttentionLayer(nn.Module):
    """
    SelfAttentionLayer: A flexible self-attention layer with multi-head attention,
    layer normalization, dropout, and optional LayerDrop.

    This layer implements multi-head self-attention with pre-layer normalization,
    dropout for regularization, and optional LayerDrop for efficiency.

    Attributes:
        embed_dim (int): Embedding dimension.
        num_heads (int): Number of attention heads.
        dropout_rate (float): Dropout rate for regularization.
        layer_drop_prob (float): Probability of dropping the layer during training.
    """
    embed_dim: int
    num_heads: int
    dropout_rate: float = 0.1
    layer_drop_prob: float = 0.1

    @validator('embed_dim')
    def check_embed_dim(cls, v):
        if v < 1:
            raise ValueError("embed_dim must be at least 1.")
        return v

    @validator('num_heads')
    def check_num_heads(cls, v):
        if v < 1:
            raise ValueError("num_heads must be at least 1.")
        return v

    @validator('dropout_rate')
    def check_dropout_rate(cls, v):
        if not 0.0 <= v < 1.0:
            raise ValueError("dropout_rate must be in the range [0.0, 1.0).")
        return v

    @validator('layer_drop_prob')
    def check_layer_drop_prob(cls, v):
        if not 0.0 <= v < 1.0:
            raise ValueError(
                "layer_drop_prob must be in the range [0.0, 1.0).")
        return v

    @nn.compact
    def __call__(self, x: jnp.ndarray, attn_mask: jnp.ndarray = None, training: bool = True) -> jnp.ndarray:
        self._validate_input(x)
        logger.debug(f"Input shape: {x.shape}")

        # Get PRNG keys for dropout and LayerDrop
        dropout_key = self.make_rng('dropout')
        layerdrop_key = self.make_rng('layerdrop')

        # Apply LayerDrop
        if training and jax.random.uniform(layerdrop_key) < self.layer_drop_prob:
            logger.debug("Applying LayerDrop: skipping this layer")
            return x

        # Apply pre-layer normalization
        normalized_x = nn.LayerNorm()(x)
        logger.debug(f"Normalized input shape: {normalized_x.shape}")

        # Perform self-attention
        attn_output = nn.SelfAttention(
            num_heads=self.num_heads,
            dropout_rate=self.dropout_rate,
            deterministic=not training
        )(normalized_x, mask=attn_mask)
        logger.debug(f"Attention output shape: {attn_output.shape}")

        # Apply dropout to attention output
        attn_output = nn.Dropout(
            rate=self.dropout_rate, deterministic=not training)(attn_output, rng=dropout_key)
        logger.debug(f"Attention output shape after dropout: {
                     attn_output.shape}")

        # Add residual connection
        x = x + attn_output
        logger.debug(f"Output shape after residual connection: {x.shape}")

        # Apply final dropout
        x = nn.Dropout(rate=self.dropout_rate,
                       deterministic=not training)(x, rng=dropout_key)
        logger.debug(f"Output shape after final dropout: {x.shape}")

        return x

    def _validate_input(self, x: jnp.ndarray):
        """Validate the input array dimensions."""
        if x.ndim != 3:
            error_msg = f"Expected input array with 3 dimensions (batch_size, seq_len, embed_dim), but got {
                x.ndim} dimensions."
            logger.error(error_msg)
            raise ValueError(error_msg)
        if x.shape[-1] != self.embed_dim:
            error_msg = f"Expected embed_dim to be {
                self.embed_dim}, but got {x.shape[-1]}."
            logger.error(error_msg)
            raise ValueError(error_msg)

    def get_config(self) -> dict:
        """
        Get the configuration of the SelfAttentionLayer.

        Returns:
            dict: A dictionary containing the layer's configuration.
        """
        config = {
            "embed_dim": self.embed_dim,
            "num_heads": self.num_heads,
            "dropout_rate": self.dropout_rate,
            "layer_drop_prob": self.layer_drop_prob
        }
        logger.debug(f"Layer config: {config}")
        return config


# Example usage
if __name__ == "__main__":
    try:
        logger.info("Starting SelfAttentionLayer example")

        # Create a sample input array
        batch_size, seq_len, embed_dim = 32, 10, 256
        x = jax.random.normal(jax.random.PRNGKey(
            0), (batch_size, seq_len, embed_dim))
        logger.info(f"Created sample input array with shape {x.shape}")

        # Initialize the SelfAttentionLayer
        layer = SelfAttentionLayer(
            embed_dim=256, num_heads=8, dropout_rate=0.1, layer_drop_prob=0.1)
        logger.info("Initialized SelfAttentionLayer")

        # Create a sample attention mask
        attn_mask = jnp.triu(jnp.ones((seq_len, seq_len)), k=1).astype(bool)
        logger.info(f"Created sample attention mask with shape {
                    attn_mask.shape}")

        # Initialize parameters
        params = layer.init(jax.random.PRNGKey(1), x, attn_mask)
        logger.info("Initialized layer parameters")

        # Perform forward pass
        output = layer.apply(params, x, attn_mask)
        logger.info(f"Performed forward pass. Output shape: {output.shape}")

        print(f"Input shape: {x.shape}")
        print(f"Output shape: {output.shape}")
        print(f"Layer config: {layer.get_config()}")

        logger.info("SelfAttentionLayer example completed successfully")
    except Exception as e:
        logger.exception(
            f"An error occurred during the SelfAttentionLayer example: {str(e)}")
