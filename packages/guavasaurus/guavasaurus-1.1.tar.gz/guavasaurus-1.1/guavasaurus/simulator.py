import itertools
import numpy as np
from .gates import QuantumGate, CNOTGate, PhaseGate, TGate, ControlledGate

class Simulator:

 H = QuantumGate.hadamard() # Hadamard
 X = QuantumGate.pauli_x()  # Pauli-X
 Y = QuantumGate.pauli_y()  # Pauli-Y
 Z = QuantumGate.pauli_z() # Pauli-Z
 T = TGate  # T-gate (π/4 phase)

# Two-qubit gates
CNOT = CNOTGate  # Controlled-NOT


# Custom gates
def custom_gate(matrix):
    """Create a custom gate given a user-defined matrix."""
    matrix = np.array(matrix)
    if matrix.shape[0] != matrix.shape[1] or np.linalg.norm(
            matrix.dot(matrix.T.conj()) - np.eye(matrix.shape[0])) > 1e-10:
        raise ValueError("The provided matrix must be unitary.")
    return matrix


# Step 2: Multi-Qubit Support
def tensor_product(gate, num_qubits, target_qubits):
    """Expand a single qubit gate to act on the specified qubits in a multi-qubit system."""
    i = np.eye(2)
    full_op = 1
    for qubit in range(num_qubits):
        if qubit in target_qubits:
            full_op = np.kron(full_op, gate)
        else:
            full_op = np.kron(full_op, i)
    return full_op


def apply_gate(state, gate, num_qubits, target_qubits):
    """Apply a quantum gate to specific qubits in the system."""
    full_op = tensor_product(gate, num_qubits, target_qubits)
    return np.dot(full_op, state)


# Step 3: Initialize a multi-qubit system
def initialize_qubits(num_qubits):
    """Initialize a quantum system of num_qubits in the |00...0> state."""
    state = np.zeros(2 ** num_qubits)
    state[0] = 1
    return state


# Step 4: Measurement
def measure(state, num_qubits):
    """Perform measurement on all qubits."""
    probabilities = np.abs(state) ** 2
    outcome = np.random.choice(len(state), p=probabilities)
    return np.binary_repr(outcome, num_qubits)


# Step 5: Add Noise (optional)
def add_noise(state, noise_level=0.01):
    """Simulate noise by adding random perturbations to the state."""
    noise = (np.random.randn(*state.shape) + 1j * np.random.randn(*state.shape)) * noise_level
    noisy_state = state + noise
    noisy_state /= np.linalg.norm(noisy_state)  # Renormalize
    return noisy_state


# Step 6: Execute a full circuit
def execute_circuit(num_qubits, gates_sequence):
    """Execute a full quantum circuit given a sequence of gates."""
    state = initialize_qubits(num_qubits)

    for gate, target_qubits in gates_sequence:
        state = apply_gate(state, gate, num_qubits, target_qubits)
        state = add_noise(state, noise_level=0.01)  # Add some noise to simulate real-world conditions

    return state


# Step 7: Visualization (text-based)
def visualize_state(state, num_qubits):
    """Visualize the state vector as probabilities of each basis state."""
    probabilities = np.abs(state) ** 2
    for i, prob in enumerate(probabilities):
        if prob > 0.01:  # Display only non-trivial probabilities
            print(f"|{np.binary_repr(i, num_qubits)}> : {prob:.4f}")