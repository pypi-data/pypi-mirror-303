# layers/snnslayer.py

import jax
import jax.numpy as jnp
from flax import linen as nn
from typing import Any, Tuple, Callable, Optional


class LIFCell(nn.Module):
    """
    Leaky Integrate-and-Fire (LIF) neuron cell.

    This class implements a single LIF neuron, which is a simplified model of a biological neuron.
    The LIF neuron integrates input over time and fires a spike when its membrane potential
    reaches a certain threshold.

    Attributes:
        tau (float): Time constant of the LIF neuron. It determines how quickly the neuron's
                     membrane potential decays in the absence of input.
        v_rest (float): Resting membrane potential. This is the potential the neuron returns to
                        in the absence of input.
        v_reset (float): Reset potential. After a spike, the neuron's potential is reset to this value.
        threshold (float): Firing threshold. If the membrane potential exceeds this value,
                           the neuron fires a spike.
        adaptive_threshold (bool): If True, use an adaptive threshold mechanism.
        threshold_adaptation_tau (float): Time constant for threshold adaptation.
    """

    tau: float = 20.0
    v_rest: float = 0.0
    v_reset: float = -65.0
    threshold: float = -50.0
    adaptive_threshold: bool = False
    threshold_adaptation_tau: float = 100.0

    @nn.compact
    def __call__(self, x: jnp.ndarray, state: Tuple[jnp.ndarray, jnp.ndarray, Optional[jnp.ndarray]]) -> Tuple[jnp.ndarray, Tuple[jnp.ndarray, jnp.ndarray, Optional[jnp.ndarray]]]:
        """
        Compute the next state of the LIF neuron.

        Args:
            x (jnp.ndarray): Input to the neuron at the current timestep.
            state (Tuple[jnp.ndarray, jnp.ndarray, Optional[jnp.ndarray]]): Current state of the neuron,
                consisting of (membrane potential, previous spikes, adaptive threshold).

        Returns:
            Tuple[jnp.ndarray, Tuple[jnp.ndarray, jnp.ndarray, Optional[jnp.ndarray]]]: A tuple containing:
                - new_spikes (jnp.ndarray): Binary array indicating whether the neuron spiked (1) or not (0).
                - new_state (Tuple[jnp.ndarray, jnp.ndarray, Optional[jnp.ndarray]]): Updated state of the neuron for the next timestep.
        """
        v, spikes, adaptive_thresh = state

        # Update membrane potential using the differential equation
        dv = (x - v + self.v_rest) / self.tau
        v = v + dv

        # Compute the effective threshold
        if self.adaptive_threshold:
            effective_threshold = self.threshold + adaptive_thresh
            dthresh = -adaptive_thresh / self.threshold_adaptation_tau + 0.1 * spikes
            adaptive_thresh = adaptive_thresh + dthresh
        else:
            effective_threshold = self.threshold

        # Detect if the firing threshold was exceeded
        new_spikes = (v >= effective_threshold).astype(jnp.float32)

        # Reset membrane potential where there was a spike
        v = jnp.where(new_spikes > 0, self.v_reset, v)

        return new_spikes, (v, new_spikes, adaptive_thresh if self.adaptive_threshold else None)


class SNNSLayer(nn.Module):
    """
    Spiking Neural Network (SNN) layer using Leaky Integrate-and-Fire (LIF) neurons.

    This layer processes input sequences through a fully connected layer followed by
    a layer of LIF neurons. It's designed to work with time-series data, processing
    each time step sequentially through the LIF neurons.

    Attributes:
        input_dim (int): Dimensionality of the input features.
        hidden_dim (int): Number of LIF neurons in the layer (hidden layer size).
        lif_params (dict): Parameters for the LIF neurons.
        activation (Callable): Activation function for the dense layer.
    """

    input_dim: int
    hidden_dim: int
    lif_params: dict = {}
    activation: Callable = nn.relu

    def setup(self):
        """
        Initialize the layer components.

        This method sets up:
        - A fully connected (dense) layer to transform input to the hidden dimension.
        - An LIF cell to process the transformed input through time.
        """
        self.fc = nn.Dense(self.hidden_dim)
        self.lif_cell = LIFCell(**self.lif_params)

    @nn.compact
    def __call__(self, x: jnp.ndarray) -> jnp.ndarray:
        """
        Process the input sequence through the SNN layer.

        Args:
            x (jnp.ndarray): Input tensor of shape (batch_size, seq_len, input_dim).

        Returns:
            jnp.ndarray: Output tensor of shape (batch_size, seq_len, hidden_dim) containing
                         the spike activities of the LIF neurons for each time step.
        """
        batch_size, seq_len, _ = x.shape

        # Initialize the state of the LIF cell
        init_state = (
            # Initial membrane potential
            jnp.zeros((batch_size, self.hidden_dim)),
            jnp.zeros((batch_size, self.hidden_dim)),  # Initial spikes
            # Initial adaptive threshold
            jnp.zeros((batch_size, self.hidden_dim)
                      ) if self.lif_cell.adaptive_threshold else None
        )

        def scan_fn(carry, x_t):
            state = carry
            z = self.activation(self.fc(x_t))
            out, new_state = self.lif_cell(z, state)
            return new_state, out

        _, outputs = jax.lax.scan(scan_fn, init_state, x.transpose(1, 0, 2))
        return outputs.transpose(1, 0, 2)

    def get_config(self):
        """
        Get the configuration of the layer.

        Returns:
            dict: A dictionary containing the configuration of the layer.
        """
        return {
            "input_dim": self.input_dim,
            "hidden_dim": self.hidden_dim,
            "lif_params": self.lif_params,
            "activation": self.activation.__name__
        }
