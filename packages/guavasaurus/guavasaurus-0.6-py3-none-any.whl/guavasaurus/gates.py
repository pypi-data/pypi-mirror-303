# gates.py
import numpy as np

class QuantumGate:
    def __init__(self, matrix):
        self.matrix = matrix

    @staticmethod
    def pauli_x():
        return QuantumGate(np.array([[0, 1], [1, 0]], dtype=complex))

    @staticmethod
    def hadamard():
        return QuantumGate((1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex))

class PhaseGate(QuantumGate):
    def __init__(self, theta):
        matrix = np.array([
            [1, 0],
            [0, np.exp(1j * theta)]
        ], dtype=complex)
        super().__init__(matrix)

class TGate(PhaseGate):
    def __init__(self):
        super().__init__(np.pi / 4)

class CNOTGate(QuantumGate):
    def __init__(self):
        super().__init__(np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ], dtype=complex))

    def apply_to(self, control_qubit, target_qubit):
        combined_state = np.kron(control_qubit.state, target_qubit.state)
        new_state = np.dot(self.matrix, combined_state)
        control_qubit.state, target_qubit.state = new_state[:2], new_state[2:]

class ControlledGate(QuantumGate):
    def __init__(self, control_qubit, target_qubit, base_gate):
        self.control_qubit = control_qubit
        self.target_qubit = target_qubit
        self.base_gate = base_gate

    def apply_to(self):
        # Apply the base gate to the target qubit if the control qubit is in the |1⟩ state
        if np.abs(self.control_qubit.state[1]) > 0:
            self.target_qubit.apply_gate(self.base_gate)
