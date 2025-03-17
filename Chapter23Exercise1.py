# Step 1: Environment Setup
from qiskit import QuantumCircuit, Aer, transpile, assemble, IBMQ, execute
from qiskit.visualization import plot_histogram
from qiskit.providers.aer import AerSimulator
import numpy as np

# Load IBM Q account
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')

# Step 2: Quantum Circuit for Key Generation using Entanglement
def generate_quantum_key():
    qc = QuantumCircuit(2, 2)
    
    # Create entanglement
    qc.h(0)
    qc.cx(0, 1)
    
    # Measure the qubits
    qc.measure([0, 1], [0, 1])
    return qc

# Step 3: Simulate the Quantum Key Generation
simulator = Aer.get_backend('qasm_simulator')
qc = generate_quantum_key()

# Transpile and assemble the circuit
tqc = transpile(qc, simulator)
qobj = assemble(tqc)

# Execute the circuit
result = simulator.run(qobj).result()
counts = result.get_counts(qc)
print("Quantum Key Counts:", counts)

# Step 4: Key Distribution using Entanglement
def distribute_keys(counts):
    keys = []
    for key, count in counts.items():
        for _ in range(count):
            keys.append(key)
    return keys

# Extract the quantum key
quantum_keys = distribute_keys(counts)
print("Distributed Quantum Keys:", quantum_keys)

# Step 5: Encrypt and Decrypt Messages
def encrypt_message(message, key):
    encrypted_message = ''.join([str(int(m)^int(k)) for m, k in zip(message, key)])
    return encrypted_message

def decrypt_message(encrypted_message, key):
    decrypted_message = ''.join([str(int(em)^int(k)) for em, k in zip(encrypted_message, key)])
    return decrypted_message

# Example usage
message = "1101"  # Binary representation of the message
key = quantum_keys[0]  # Using the first key for simplicity

encrypted_message = encrypt_message(message, key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, key)
print("Decrypted Message:", decrypted_message)

# Step 6: Run and Validate on IBM Quantum Computer
backend = provider.get_backend('ibmq_qasm_simulator')
tqc = transpile(qc, backend)
qobj = assemble(tqc)

job = backend.run(qobj)
result = job.result()

counts = result.get_counts(qc)
print("Quantum Key Counts from IBM Q:", counts)

# Distribute keys from IBM Q result
quantum_keys_ibm = distribute_keys(counts)
print("Distributed Quantum Keys from IBM Q:", quantum_keys_ibm)

# Validate encryption and decryption using IBM Q keys
key_ibm = quantum_keys_ibm[0]  # Using the first key from IBM Q
encrypted_message_ibm = encrypt_message(message, key_ibm)
print("Encrypted Message with IBM Q Key:", encrypted_message_ibm)

decrypted_message_ibm = decrypt_message(encrypted_message_ibm, key_ibm)
print("Decrypted Message with IBM Q Key:", decrypted_message_ibm)
