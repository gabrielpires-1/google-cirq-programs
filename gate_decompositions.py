import cirq

# Circuito com a operação Hadamard
print('Hadamard Gate')
print(cirq.Circuit(cirq.H(cirq.LineQubit(0))))
print('\n')

# Circuito com a operação Hadamard decomposta em potas X e Y
print('Hadamard gate decomposed as X and Y gates')
print(cirq.Circuit(cirq.decompose(cirq.Circuit(cirq.H(cirq.LineQubit(0))))))

# Circuito com a operação Toffoli
print('\nToffoli Gate')
print(cirq.Circuit(cirq.T(cirq.LineQubit(0))))
print('\n')

# Circuito com a operação Toffoli decomposta
print('Toffoli Gate decomposed as X and Y gates')
q0, q1, q2 = cirq.LineQubit.range(3)
print(cirq.Circuit(cirq.decompose(cirq.TOFFOLI(q0, q1, q2))))
