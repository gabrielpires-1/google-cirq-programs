import cirq

# Definir um qubit
q0 = cirq.LineQubit(0)

# Definir um circuito que aplica a porta Hadamard seguida da medição
circuit = cirq.Circuit(cirq.H(q0), cirq.measure(q0))

# Executar o circuito 1 vez em um simulador
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1)

# Imprimir o resultado
print(result)
 