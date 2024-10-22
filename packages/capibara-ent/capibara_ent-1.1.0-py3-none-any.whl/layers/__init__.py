# layers/__init__.py

"""
layers Module: Contains all the custom layers used in the Capibara project.

Available Classes:
    - BitnetQuantizer: Implements a quantization layer for the Bitnet network.
    - Bitnet: Implements the Bitnet network architecture.
    - GamesTheory: Implements a game theory-based layer.
    - Liquid: Implements a Liquid-type layer.
    - MambaByte: Implements a Mamba Byte-type layer.
    - Mamba2: Implements the Mamba2 network architecture.
    - MetaMamdp: Implements a Meta-MAMDP-type layer.
    - SparseMamba: Implements a layer optimized for sparse operations on TPUs.
    - SyntheticEmbedding: Creates synthetic representations through linear transformations and GELU activations.
    - SelfAttention: Implements a self-attention layer with pre-layer normalization and dropout.
    
auto-atención con normalización pre-capa y dropout.
"""

from .synthetic_embedding import SyntheticEmbeddingLayer
from .convolutional_layer import ConvolutionalLayer
from .attention_layer import AttentionLayer
from .sparse_mamba_layer import SparseMambaLayer
from .self_attention_layer import SelfAttentionLayer
from .bitnet_quantizer import BitnetQuantizer
from .bitnet import Bitnet
from .games_theory import GamesTheory
from .liquid import Liquid
from .mamba_byte import MambaByte
from .mamba2 import Mamba2
from .meta_mamdp import MetaMamdp
from .sparse_mamba import SparseMamba
from .synthetic_embedding import SyntheticEmbedding
from .self_attention import SelfAttention

__all__ = [
    'SyntheticEmbeddingLayer',
    'ConvolutionalLayer',
    'AttentionLayer',
    'SparseMambaLayer',
    'SelfAttentionLayer',
    'BitnetQuantizer',
    'Bitnet',
    'GamesTheory',
    'Liquid',
    'MambaByte',
    'Mamba2',
    'MetaMamdp',
    'SparseMamba',
    'SyntheticEmbedding',
    'SelfAttention',
]
