import cirq

print('Unitary of the X gate')
print(cirq.unitary(cirq.X))

print('\n')

print('Unitary of the Z gate')
print(cirq.unitary(cirq.Z))

print('\n')

print('Unitary of the H gate')
print(cirq.unitary(cirq.H))

print('\n')

print('Unitary of SWAP operator on two qubits.')
q0, q1 = cirq.LineQubit.range(2)
print(cirq.unitary(cirq.SWAP(q0, q1)))

print('\n')

print('Unitary of a sample circuit')
print(cirq.unitary(cirq.Circuit(cirq.X(q0), cirq.SWAP(q0, q1))))
