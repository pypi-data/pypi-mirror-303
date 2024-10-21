import numpy as np
from .circuit import QuantumCircuit
from .gates import QuantumGate, PhaseGate

class GroverCircuit(QuantumCircuit):
    def __init__(self, num_qubits, oracle):
        super().__init__(num_qubits)
        if oracle.matrix.shape != (2 ** num_qubits, 2 ** num_qubits):
            raise ValueError("Oracle size must match the number of qubits.")
        self.oracle = oracle
        self.diffusion_gate = self._create_diffusion_operator()

    def _create_diffusion_operator(self):
        n = 2 ** self.num_qubits
        s = np.ones((n, n), dtype=complex) / n
        I = np.eye(n, dtype=complex)
        return QuantumGate(2 * s - I)

    def build_grover_circuit(self):
        for i in range(self.num_qubits):
            self.add_gate(QuantumGate.hadamard(), [i])
        self.add_gate(self.oracle, list(range(self.num_qubits)))
        self.add_gate(self.diffusion_gate, list(range(self.num_qubits)))





class QFTCircuit(QuantumCircuit):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def apply_qft(self):
        for i in range(self.num_qubits):
            self.add_gate(QuantumGate.hadamard(), [i])
            for j in range(i + 1, self.num_qubits):
                theta = np.pi / (2 ** (j - i))
                self.add_gate(PhaseGate(theta), [j])

    def execute(self):
        super().execute()
        return self.measure_all()


class QuantumDeletionTheory:

    @staticmethod
    def initialize_qubit(state):
        """
        Initialize a qubit in a given state.
        'state' is a tuple of the form (alpha, beta) where |alpha|^2 + |beta|^2 = 1.
        """
        alpha, beta = state
        return np.array([alpha, beta])

    @staticmethod
    def apply_dissipation(state, eta):
        """
        Apply energy dissipation to a quantum state.
        'eta' is the dissipation factor, where 0 <= eta <= 1.
        """
        return eta * state

    @staticmethod
    def fidelity(state1, state2):
        """
        Calculate the fidelity between two quantum states.
        Fidelity is defined as F = |<psi1 | psi2>|^2.
        """
        return np.abs(np.dot(np.conjugate(state1), state2)) ** 2

    @staticmethod
    def calculate_information_loss(eta):
        """
        Calculate information loss based on the dissipation factor.
        L = 1 - eta^2
        """
        return 1 - eta ** 2
