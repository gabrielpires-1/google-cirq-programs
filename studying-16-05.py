import cirq

circuit = cirq.Circuit()
qubits = cirq.LineQubit.range(3)
circuit.append(cirq.H(qubits[0])) # this is a operation
circuit.append(cirq.H(qubits[1])) # this is a operation
circuit.append(cirq.H(qubits[2])) # this is a operation
print(circuit)

# Other way 
'''
circuit = cirq.Circuit()
ops = [cirq.H(q) for q in cirq.LineQubit.range(3)]
circuit.append(ops)
print(circuit)
'''