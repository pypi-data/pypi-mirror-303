# tests/test_layers.py

import jax.numpy as jnp
import pytest
import torch
from capibara.layers import (
    MambaByteLayer,
    SyntheticEmbeddingLayer,
    BitnetLayer,
    LiquidLayer,
    SparseMambaLayer,
    Mamba2Layer,
    BitNetQuantizer,
    MetaBAMDPLayer,
    SNNSLayer, OckhamLayer,
    PlatonicLayer,
    GameTheoryLayer
)


def test_ockham_layer():
    input_dim = 256
    hidden_dim = 512
    layer = OckhamLayer(input_dim=input_dim, hidden_dim=hidden_dim)
    input_tensor = jnp.ones((1, input_dim))
    output, _ = layer(input_tensor)
    assert output.shape == (1, hidden_dim), f"Forma de salida inesperada: {
        output.shape}"


def test_platonic_layer():
    input_dim = 128
    hidden_dim = 256
    layer = PlatonicLayer(input_dim=input_dim, hidden_dim=hidden_dim)
    input_tensor = jnp.ones((1, input_dim))
    output = layer(input_tensor)
    assert output.shape == (1, hidden_dim), f"Forma de salida inesperada: {
        output.shape}"


def test_game_theory_layer():
    input_dim = 64
    hidden_dim = 128
    layer = GameTheoryLayer(input_dim=input_dim, hidden_dim=hidden_dim)
    input_tensor = jnp.ones((1, input_dim))
    output = layer(input_tensor)
    assert output.shape == (1, hidden_dim), f"Forma de salida inesperada: {
        output.shape}"


def test_mamba_byte_layer():
    layer = MambaByteLayer(input_dim=64, output_dim=128)
    input_tensor = torch.randn(32, 64)  # batch_size=32, input_dim=64
    output = layer(input_tensor)
    assert output.shape == (32, 128), f"Forma de salida inesperada: {
        output.shape}"


def test_synthetic_embedding_layer():
    layer = SyntheticEmbeddingLayer(input_dim=128)
    input_tensor = torch.randint(0, 128, (32, 10))  # batch_size=32, seq_len=10
    output = layer(input_tensor)
    assert output.shape == (32, 10, 128), f"Forma de salida inesperada: {
        output.shape}"

# Añade más pruebas para las otras capas de manera similar


@pytest.fixture
def model_params(capibara_model, rng_key):
    """
    Pytest fixture that provides initialized parameters for the CapibaraTextGenerator model.

    This fixture can be used in test functions to get fresh initialized parameters
    for each test, ensuring test isolation.

    Returns:
        Any: The initialized parameters of the model.
    """
    return init_model_params(rng_key, capibara_model)
