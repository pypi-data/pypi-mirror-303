# algorithms.py
import numpy as np
from .circuit import QuantumCircuit
from .gates import QuantumGate, PhaseGate

class GroverCircuit(QuantumCircuit):
    def __init__(self, num_qubits, oracle):
        super().__init__(num_qubits)
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
