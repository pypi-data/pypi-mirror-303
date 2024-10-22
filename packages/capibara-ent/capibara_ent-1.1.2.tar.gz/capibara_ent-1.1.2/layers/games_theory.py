"""
Module that implements a Game Theory layer for neural networks using JAX/Flax.

This module provides an implementation of the Game Theory layer, which applies
game theory concepts to analyze and process input data.

Classes:
    GameTheoryLayer: Implements a Game Theory layer.

Dependencies:
    - jax: For array operations and automatic differentiation.
    - flax: For neural network module definitions.
    - numpy: For numerical operations.
"""

import jax
import jax.numpy as jnp
from flax import linen as nn
from typing import Dict, Tuple, List, Any
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GameTheoryError(Exception):
    """Custom exception for Game Theory related errors."""
    pass

class GameTheoryLayer(nn.Module):
    """
    A Game Theory layer implementation that applies game theory concepts to input data.

    This layer provides methods to analyze different game theory scenarios and
    determine optimal strategies based on the input.

    Attributes:
        strategies (Dict[str, callable]): Dictionary of game theory strategies and their implementations.
    """

    def setup(self):
        self.strategies = {
            "prisoners_dilemma": self.prisoners_dilemma,
            "minimax": self.minimax,
            "nash_equilibrium": self.nash_equilibrium,
            "dominant_strategy": self.dominant_strategy,
            "mixed_strategy": self.mixed_strategy
        }
        logger.info("GameTheoryLayer initialized with strategies: %s", list(self.strategies.keys()))

    @nn.compact
    def __call__(self, game_type: str, *args: Any) -> Any:
        """
        Forward pass of the GameTheoryLayer.

        Args:
            game_type (str): Type of game to analyze.
            *args: Arguments needed for the specific game.

        Returns:
            Any: Result of the strategic analysis.
        """
        logger.debug("Calling GameTheoryLayer with game_type: %s", game_type)
        return self.process_input(game_type, *args)

    def prisoners_dilemma(self, player_strategy: str, opponent_strategy: str) -> Tuple[int, int]:
        """
        Simulates a simple Prisoner's Dilemma game with two players.

        Args:
            player_strategy (str): Strategy of the player ('cooperate' or 'defect').
            opponent_strategy (str): Strategy of the opponent ('cooperate' or 'defect').

        Returns:
            Tuple[int, int]: Payoffs for the player and the opponent.
        """
        logger.debug("Simulating Prisoner's Dilemma with strategies: %s, %s", player_strategy, opponent_strategy)
        payoff_matrix = {
            ("cooperate", "cooperate"): (3, 3),
            ("cooperate", "defect"): (0, 5),
            ("defect", "cooperate"): (5, 0),
            ("defect", "defect"): (1, 1)
        }
        result = payoff_matrix[(player_strategy, opponent_strategy)]
        logger.info("Prisoner's Dilemma result: %s", result)
        return result

    @jax.jit
    def minimax(self, payoff_matrix: jnp.ndarray) -> Tuple[int, float]:
        """
        Implements the Minimax algorithm to determine the optimal strategy.

        Args:
            payoff_matrix (jnp.ndarray): Payoff matrix of the game.

        Returns:
            Tuple[int, float]: Optimal strategy and expected value.
        """
        logger.debug("Applying Minimax algorithm to payoff matrix")
        min_values = jnp.min(payoff_matrix, axis=1)
        max_of_min = jnp.max(min_values)
        optimal_strategy = jnp.argmax(min_values)
        result = (int(optimal_strategy), float(max_of_min))
        logger.info("Minimax result: %s", result)
        return result

    @jax.jit
    def nash_equilibrium(self, payoff_matrix: jnp.ndarray) -> List[Tuple[int, int]]:
        """
        Finds Nash equilibria in a two-player game.

        Args:
            payoff_matrix (jnp.ndarray): Payoff matrix of the game with shape (rows, cols, 2).

        Returns:
            List[Tuple[int, int]]: Nash equilibrium strategies.
        """
        logger.debug("Finding Nash equilibria in payoff matrix with shape %s", payoff_matrix.shape)
        
        rows, cols, _ = payoff_matrix.shape
        nash_eq = []

        for i in range(rows):
            for j in range(cols):
                player_payoff = payoff_matrix[i, j, 0]
                opponent_payoff = payoff_matrix[i, j, 1]

                # Verificar si i es la mejor respuesta para el jugador
                best_response_player = jnp.argmax(payoff_matrix[:, j, 0])
                # Verificar si j es la mejor respuesta para el oponente
                best_response_opponent = jnp.argmax(payoff_matrix[i, :, 1])

                if i == best_response_player and j == best_response_opponent:
                    nash_eq.append((i, j))
                    logger.debug("Found Nash equilibrium at (%d, %d) with payoffs (%f, %f)", 
                                 i, j, player_payoff, opponent_payoff)

        logger.info("Found %d Nash equilibria", len(nash_eq))
        return nash_eq

    @jax.jit
    def dominant_strategy(self, payoff_matrix: jnp.ndarray) -> Tuple[int, int]:
        """
        Finds dominant strategies for both players.

        Args:
            payoff_matrix (jnp.ndarray): Payoff matrix of the game.

        Returns:
            Tuple[int, int]: Dominant strategies for row and column players.
        """
        logger.debug("Finding dominant strategies in payoff matrix")
        row_dominant = jnp.all(payoff_matrix >= jnp.max(payoff_matrix, axis=1, keepdims=True), axis=1)
        col_dominant = jnp.all(payoff_matrix >= jnp.max(payoff_matrix, axis=0, keepdims=True), axis=0)

        row_strategy = jnp.argmax(row_dominant)
        col_strategy = jnp.argmax(col_dominant)

        result = (int(row_strategy), int(col_strategy))
        logger.info("Dominant strategies found: %s", result)
        return result

    def mixed_strategy(self, payoff_matrix: jnp.ndarray) -> Tuple[jnp.ndarray, jnp.ndarray]:
        """
        Calculates mixed strategy Nash equilibrium for a 2x2 game.

        Args:
            payoff_matrix (jnp.ndarray): Payoff matrix of the game.

        Returns:
            Tuple[jnp.ndarray, jnp.ndarray]: Mixed strategies for row and column players.
        """
        logger.debug("Calculating mixed strategy Nash equilibrium")
        if payoff_matrix.shape != (2, 2):
            error_msg = "Mixed strategy is only implemented for 2x2 games"
            logger.error(error_msg)
            raise GameTheoryError(error_msg)

        a, b, c, d = payoff_matrix.flatten()

        p = (d - b) / (a - b - c + d)
        q = (d - c) / (a - b - c + d)

        result = (jnp.array([p, 1-p]), jnp.array([q, 1-q]))
        logger.info("Mixed strategy Nash equilibrium calculated: %s", result)
        return result

    def process_input(self, game_type: str, *args: Any) -> Any:
        """
        Processes the input using game theory based on the specified game type.

        Args:
            game_type (str): Type of game to analyze.
            *args: Arguments needed for the game.

        Returns:
            Any: Result of the strategic analysis.

        Raises:
            GameTheoryError: If the game type is not supported or if there's an error in processing.
        """
        logger.debug("Processing input for game type: %s", game_type)
        if game_type not in self.strategies:
            error_msg = f"Unsupported game type: {game_type}"
            logger.error(error_msg)
            raise GameTheoryError(error_msg)

        try:
            if game_type == "nash_equilibrium":
                payoff_matrix = args[0]
                if payoff_matrix.ndim != 3 or payoff_matrix.shape[2] != 2:
                    error_msg = f"Invalid payoff matrix shape for Nash equilibrium. Expected (rows, cols, 2), got {payoff_matrix.shape}"
                    logger.error(error_msg)
                    raise GameTheoryError(error_msg)
            
            result = self.strategies[game_type](*args)
            logger.info("Successfully processed game %s", game_type)
            return result
        except Exception as e:
            error_msg = f"Error processing game {game_type}: {str(e)}"
            logger.error(error_msg)
            raise GameTheoryError(error_msg) from e

    def get_config(self) -> Dict[str, Any]:
        """
        Gets the configuration of the GameTheoryLayer.

        Returns:
            Dict[str, Any]: A dictionary containing the layer's configuration.
        """
        return {
            "supported_strategies": list(self.strategies.keys())
        }

    def interpret_result(self, game_type: str, result: Any) -> str:
        """
        Interprets the result of the game theory analysis.

        Args:
            game_type (str): Type of game analyzed.
            result (Any): Result of the analysis.

        Returns:
            str: A natural language interpretation of the result.
        """
        logger.debug("Interpreting result for game type: %s", game_type)
        interpretation = "Unable to interpret the result for this game type."
        
        if game_type == "prisoners_dilemma":
            player, opponent = result
            if player > opponent:
                interpretation = f"In the Prisoner's Dilemma, the player achieves a better outcome ({player}) than the opponent ({opponent}). This suggests the player chose a more effective strategy."
            elif player < opponent:
                interpretation = f"In the Prisoner's Dilemma, the opponent achieves a better outcome ({opponent}) than the player ({player}). This suggests the opponent chose a more effective strategy."
            else:
                interpretation = f"In the Prisoner's Dilemma, both players achieve the same outcome ({player}). This suggests they chose similar strategies."
        elif game_type == "minimax":
            strategy, value = result
            interpretation = f"The optimal Minimax strategy is strategy {strategy}, which guarantees a minimum value of {value}. This represents the best defensive strategy in the worst-case scenario."
        elif game_type == "nash_equilibrium":
            if not result:
                interpretation = "No pure Nash equilibria were found in this game."
            elif len(result) == 1:
                interpretation = f"A single pure Nash equilibrium was found at {result[0]}. This is the strategy profile that no player has an incentive to unilaterally deviate from."
            else:
                interpretation = f"Multiple pure Nash equilibria were found: {result}. This suggests the game has multiple points of strategic stability."
        elif game_type == "dominant_strategy":
            row, col = result
            interpretation = f"The dominant strategy for the row player is {row}, and for the column player is {col}. These are the best strategies regardless of what the other player does."
        elif game_type == "mixed_strategy":
            p, q = result
            interpretation = f"The optimal mixed strategy for the row player is to play the first strategy with probability {p[0]:.2f} and the second with {p[1]:.2f}. For the column player, the probabilities are {q[0]:.2f} and {q[1]:.2f} respectively."
        
        logger.info("Result interpretation: %s", interpretation)
        return interpretation


# Example usage
if __name__ == "__main__":
    try:
        logger.info("Starting GameTheoryLayer example")

        # Initialize the GameTheoryLayer
        layer = GameTheoryLayer()
        logger.info("GameTheoryLayer initialized")

        # Initialize parameters
        params = layer.init(jax.random.PRNGKey(0), "nash_equilibrium", jnp.zeros((2, 2, 2)))
        logger.info("Parameters initialized")

        # Test Nash Equilibrium
        payoff_matrix = jnp.array([
            [[3, 3], [0, 5]],
            [[5, 0], [1, 1]]
        ])
        ne_result = layer.apply(params, "nash_equilibrium", payoff_matrix)
        print("Nash Equilibria:", ne_result)
        print("Interpretation:", layer.interpret_result("nash_equilibrium", ne_result))

        # Print layer configuration
        print("Layer config:", layer.get_config())

        logger.info("GameTheoryLayer example completed successfully")
    except Exception as e:
        logger.exception("An error occurred during the GameTheoryLayer example: %s", str(e))
