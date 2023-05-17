import cirq
import matplotlib.pyplot as plt

# Crie um circuito que gera um Bell State
# 1/sqrt(2) * ( |00⟩ + |11⟩ )

bell_circuit = cirq.Circuit() # declara o circuito
q0, q1 = cirq.LineQubit.range(2) # declara os qubits como uma lista de qubits numerados de 0 a 1
bell_circuit.append(cirq.H(q0)) # aplica a porta Hadamard no qubit q0
bell_circuit.append(cirq.CNOT(q0, q1)) # adiciona a porta CNOT ao circuito, controlada pelo qubit q0 e alvo no qubit q1

# Mostra o circuito
print(bell_circuit)
print('\n')

# Inicializa o simulador
simulator = cirq.Simulator()

print('Simulate the circuit:')
results = simulator.simulate(bell_circuit) # simula o circuito 'bell_circuit' no simulador
print(results) 

# Realiza a operação de medição no circuito, com a chave de identificação 'result'
bell_circuit.append(cirq.measure(q0, q1, key='result'))

# Executa o circuito 1000 vezes e armazena os resultados em 'samples'
samples = simulator.run(bell_circuit, repetitions=1000)

# Mostra o circuito agora com a operação 'medição'
print(bell_circuit)
print('\n')

# Quantidade de medições com identificação 'result' armazenadas na variável histogram
histogram = samples.histogram(key='result')
print(histogram)

# Printa o número de vezes que determinado resultado apareceu. Nesse caso, só existem das opções: 3 ou 2
for result, count in histogram.items():
    print(f"Resultado: {result}, Contagem: {count}")

# Gráfico do histograma
cirq.plot_state_histogram(histogram, plt.subplot())
plt.show()
