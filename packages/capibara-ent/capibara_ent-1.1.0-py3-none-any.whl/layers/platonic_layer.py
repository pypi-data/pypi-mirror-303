"""
Module that implements a Platonic layer for neural networks using JAX/Flax.

This module provides an implementation of the Platonic layer, which uses
sentence embeddings to transform input text into abstract concepts or ideas.

Classes:
    PlatonicLayer: Implements a Platonic layer.

Dependencies:
    - jax: For array operations and automatic differentiation.
    - flax: For neural network module definitions.
    - sentence_transformers: For generating sentence embeddings.
"""

import jax
import jax.numpy as jnp
from flax import linen as nn
from sentence_transformers import SentenceTransformer
import logging
from typing import List, Dict, Tuple
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)


class PlatonicLayer(nn.Module):
    """
    A Platonic layer implementation that transforms text into abstract concepts.

    This layer uses sentence embeddings to compare input text with predefined
    archetypal concepts and determine the most relevant abstract idea.

    Attributes:
        embedding_model (SentenceTransformer): Model for generating sentence embeddings.
        archetypes (Dict[str, jnp.ndarray]): Dictionary of archetypal concepts and their embeddings.
        similarity_threshold (float): Threshold for considering an idea as relevant.
    """

    embedding_model: SentenceTransformer
    similarity_threshold: float = 0.5

    def setup(self):
        self.archetypes = self.generate_archetypes()

    def generate_archetypes(self) -> Dict[str, jnp.ndarray]:
        """
        Generates a collection of archetypes as ideal vectors representing universal concepts.
        """
        concepts = os.getenv('CAPIBARA_PLATONIC_CONCEPTS',
                             "Justice,Beauty,Goodness,Truth").split(',')
        archetypes = {concept: jnp.array(
            self.embedding_model.encode(concept)) for concept in concepts}
        return archetypes

    @nn.compact
    def __call__(self, x: str) -> Tuple[str, float, Dict[str, float]]:
        """
        Forward pass of the PlatonicLayer.

        Args:
            x (str): Input text.

        Returns:
            Tuple[str, float, Dict[str, float]]: A tuple containing the main idea,
            its similarity score, and a dictionary of all similarities.
        """
        self._validate_input(x)

        input_embedding = jnp.array(self.embedding_model.encode(x))
        main_idea, similarity, all_similarities = self.transform_to_idea(
            input_embedding)

        return main_idea, similarity, all_similarities

    @jax.jit
    def cosine_similarity(self, vector1: jnp.ndarray, vector2: jnp.ndarray) -> float:
        """
        Calculates the cosine similarity between two vectors.
        """
        return jnp.dot(vector1, vector2) / (jnp.linalg.norm(vector1) * jnp.linalg.norm(vector2))

    def transform_to_idea(self, input_embedding: jnp.ndarray) -> Tuple[str, float, Dict[str, float]]:
        """
        Transforms the input embedding into an abstract concept (idea) by comparing it with the archetypes.
        """
        similarities = {key: self.cosine_similarity(input_embedding, archetype).item()
                        for key, archetype in self.archetypes.items()}

        main_idea = max(similarities, key=similarities.get)
        max_similarity = similarities[main_idea]

        return main_idea, max_similarity, similarities

    def _validate_input(self, x: str):
        """Validates the input text."""
        if not isinstance(x, str):
            raise ValueError(
                f"Expected input to be a string, but got {type(x)}.")
        if len(x) == 0:
            raise ValueError("Input string cannot be empty.")

    def get_config(self) -> Dict[str, any]:
        """
        Gets the configuration of the PlatonicLayer.

        Returns:
            Dict[str, any]: A dictionary containing the layer's configuration.
        """
        return {
            "embedding_model": self.embedding_model.__class__.__name__,
            "archetypes": list(self.archetypes.keys()),
            "similarity_threshold": self.similarity_threshold
        }

    def interpret_result(self, main_idea: str, similarity: float, all_similarities: Dict[str, float]) -> str:
        """
        Interprets the result of the idea transformation.

        Args:
            main_idea (str): The main idea identified.
            similarity (float): The similarity score of the main idea.
            all_similarities (Dict[str, float]): Dictionary of all similarities.

        Returns:
            str: A natural language interpretation of the result.
        """
        if similarity < self.similarity_threshold:
            return f"The text does not strongly align with any Platonic concept. The closest idea is '{main_idea}' with a similarity of {similarity:.2f}."

        other_ideas = [f"'{idea}' ({sim:.2f})" for idea,
                       sim in all_similarities.items() if idea != main_idea]
        return f"The text primarily aligns with the Platonic concept of '{main_idea}' (similarity: {similarity:.2f}). It also shows some alignment with {', '.join(other_ideas)}."


# Example usage
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Initialize the embedding model
    embedding_model = SentenceTransformer(
        os.getenv('CAPIBARA_EMBEDDING_MODEL', 'all-MiniLM-L6-v2'))

    # Initialize the PlatonicLayer
    layer = PlatonicLayer(embedding_model)

    # Initialize parameters
    params = layer.init(jax.random.PRNGKey(0), "Test input")

    # Perform forward pass
    input_text = "The importance of truth in today's society"
    main_idea, similarity, all_similarities = layer.apply(params, input_text)

    print(f"Input text: {input_text}")
    print(f"Main idea: {main_idea}")
    print(f"Similarity score: {similarity}")
    print(f"All similarities: {all_similarities}")
    print(f"Interpretation: {layer.interpret_result(
        main_idea, similarity, all_similarities)}")
    print(f"Layer config: {layer.get_config()}")