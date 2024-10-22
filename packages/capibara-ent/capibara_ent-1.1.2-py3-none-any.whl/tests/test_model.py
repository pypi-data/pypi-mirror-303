# tests/test_model.py

import pytest
import jax
import jax.numpy as jnp
from capibara.models.model import CapibaraENT
from capibara.config import CapibaraConfig


def test_model_creation(capibara_model, test_config):
    """
    Test if the model is correctly instantiated as a CapibaraENT.
    """
    assert isinstance(
        capibara_model, CapibaraENT), "The model is not an instance of CapibaraENT"
    assert capibara_model.config == test_config, "The model's configuration does not match the test configuration"


def test_forward_pass(capibara_model, model_params, sample_input):
    """
    Test the forward pass of the model.
    """
    # Create a sample attention mask
    attention_mask = jnp.ones_like(sample_input)

    # Run the forward pass
    output = capibara_model.apply(
        {'params': model_params}, sample_input, attention_mask=attention_mask)

    assert 'output' in output, "The model output does not contain the 'output' key"
    assert 'layer_outputs' in output, "The model output does not contain the 'layer_outputs' key"
    expected_shape = (1, capibara_model.config.max_length,
                      capibara_model.config.vocab_size)
    assert output['output'].shape == expected_shape, f"Unexpected output shape: {
        output['output'].shape}, expected: {expected_shape}"


def test_generate_response(capibara_model, model_params, rng_key):
    """
    Test the response generation functionality of the model.
    """
    user_input = "Hello, how are you?"
    conversation_history = ["User: Hello, how are you?"]

    # Call the response generation function
    response = capibara_model.apply({'params': model_params}, user_input, conversation_history,
                                    method=capibara_model.generate_response, rngs={'dropout': rng_key})

    assert isinstance(response, str), "The generated response is not a string"
    assert len(response) > 0, "The generated response is empty"


@pytest.mark.parametrize("input_text,expected_lang", [
    ("Hello, how are you?", "en"),
    ("Hola, ¿cómo estás?", "es"),
    ("Bonjour, comment allez-vous?", "fr"),
])
def test_language_detection(capibara_model, model_params, input_text, expected_lang):
    """
    Test the language detection functionality of the model.
    """
    detected_lang = capibara_model.apply(
        {'params': model_params}, input_text, method=capibara_model.detect_language)
    assert detected_lang == expected_lang, f"Expected {
        expected_lang}, but got {detected_lang} for '{input_text}'"


def test_translation(capibara_model, model_params):
    """
    Test the translation functionality of the model.
    """
    input_text = "Hello, world!"
    source_lang = "en"
    target_lang = "es"

    translated = capibara_model.apply(
        {'params': model_params}, input_text, source_lang, target_lang, method=capibara_model.translate)

    assert isinstance(translated, str), "The translated text is not a string"
    assert translated != input_text, "The translated text is the same as the input text"
    assert len(translated) > 0, "The translated text is empty"
