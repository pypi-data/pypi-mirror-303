import unittest
import jax
import jax.numpy as jnp
from jax import random
from flax import linen as nn

from capibara.config import CapibaraConfig
from capibara.models.model import CapibaraENT
from capibara.utils.activations import gelu, swish
from capibara.utils.positional_encoding import PositionalEncoding
from capibara.utils.mask import create_masks
from capibara.utils.language_utils import detect_language, translate_text


class TestCapibaraENT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test environment for all test methods in the class."""
        cls.rng = random.PRNGKey(0)

    def setUp(self):
        """Sets up the test environment for each test method."""
        self.config = CapibaraConfig(
            d_model=512,
            d_state=256,
            d_conv=128,
            expand=2,
            base_model_name='gpt2',
            translation_model='facebook/m2m100_418M',
            get_active_layers=lambda: ['platonic', 'game_theory', 'ethics'],
            get_layer_config=lambda layer_name: {},
            personality={},
            context_window_size=10,
            max_length=50,
            vocab_size=1000
        )
        self.model = CapibaraENT(self.config)

    def test_model_creation(self):
        """Tests the creation of the CapibaraENT model."""
        self.assertIsInstance(self.model, CapibaraENT)

    def test_forward_pass(self):
        """Tests a forward pass through the model."""
        rng, input_rng = random.split(self.rng)
        input_ids = random.randint(
            input_rng, (1, self.config.max_length), 0, self.config.vocab_size)

        variables = self.model.init(rng, input_ids)
        output = self.model.apply(variables, input_ids)

        self.assertEqual(
            output['output'].shape, (1, self.config.max_length, self.config.vocab_size))

    def test_generate_response(self):
        """Tests the response generation."""
        rng, input_rng = random.split(self.rng)
        variables = self.model.init(rng, jnp.ones(
            (1, self.config.max_length), dtype=jnp.int32))

        user_input = "Hello, how are you?"
        conversation_history = ["User: Hi",
                                "AI: Hello! How can I assist you today?"]

        response = self.model.apply(
            variables, user_input, conversation_history, method=self.model.generate_response)

        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def test_gelu(self):
        """Tests the GELU activation function."""
        x = jnp.array([-2.0, -1.0, 0.0, 1.0, 2.0])
        output = gelu(x)
        expected = jnp.array(
            [-0.04550026, -0.15865529, 0.0, 0.8413447, 1.9544997])
        self.assertTrue(jnp.allclose(output, expected, atol=1e-6))

    def test_swish(self):
        """Tests the Swish activation function."""
        x = jnp.array([-2.0, -1.0, 0.0, 1.0, 2.0])
        output = swish(x)
        expected = jnp.array(
            [-0.23840584, -0.26894143, 0.0, 0.7310586, 1.7615942])
        self.assertTrue(jnp.allclose(output, expected, atol=1e-6))

    def test_positional_encoding(self):
        """Tests the positional encoding."""
        max_len, d_model = 100, 512
        pe = PositionalEncoding(d_model, max_len=max_len)
        encoding = pe(jnp.zeros((1, max_len, d_model)))
        self.assertEqual(encoding.shape, (1, max_len, d_model))
        self.assertTrue(jnp.all(encoding >= -1) and jnp.all(encoding <= 1))

    def test_create_masks(self):
        """Tests the creation of masks."""
        seq_len, batch_size = 10, 2
        src_mask, tgt_mask = create_masks(seq_len, batch_size)
        self.assertEqual(src_mask.shape, (batch_size, 1, seq_len))
        self.assertEqual(tgt_mask.shape, (batch_size, seq_len, seq_len))

    def test_detect_language(self):
        """Tests the language detection function."""
        text = "Hello, how are you?"
        lang = detect_language(text)
        self.assertEqual(lang, "en")

    def test_translate_text(self):
        """Tests the text translation function."""
        text = "Hello, how are you?"
        translated = translate_text(text, source_lang="en", target_lang="es")
        self.assertIsInstance(translated, str)
        self.assertNotEqual(text, translated)


if __name__ == '__main__':
    unittest.main()
