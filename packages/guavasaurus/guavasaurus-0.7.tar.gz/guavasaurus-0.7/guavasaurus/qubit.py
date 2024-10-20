# qubit.py
import numpy as np

class Qubit:
    def __init__(self, index):
        self.index = index
        self.state = np.array([1, 0], dtype=complex)  # Start in the |0⟩ state

    def apply_gate(self, gate):
        self.state = np.dot(gate.matrix, self.state)

    def measure(self):
        probabilities = np.abs(self.state) ** 2
        probabilities /= np.sum(probabilities)  # Normalize probabilities
        result = np.random.choice([0, 1], p=probabilities)
        return result
