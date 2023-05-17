import sympy, cirq 
import matplotlib.pyplot as plt

# sympy é uma biblioteca para manipulação simbólica usada para representar um símbolo variável 't'.

# Aplica a porta X com um expoente variável
q = cirq.GridQubit(1, 1)
circuit = cirq.Circuit(cirq.X(q) ** sympy.Symbol('t'), cirq.measure(q, key='m'))

# Criação de um intervalo linear de valores para o símbolo 't' usando cirq.Linspace.
# O sweep de parâmetros vai de 0 a 2, dividido em 200 pontos igualmente espaçados.  
param_sweep = cirq.Linspace('t', start=0, stop=2, length=200)

# Simula o circuito com o sweep
s = cirq.Simulator()
# A função run_sweep executa o circuito várias vezes, cada vez com um valor diferente de 't' no sweep.
# Para cada execução, são realizadas 1000 repetições para coletar estatísticas estocásticas.
trials = s.run_sweep(circuit, param_sweep, repetitions=1000)

# Mostra os resultados
# Para cada execução do circuito, os valores de 't' e a frequência em que o qubit é medido como '1' são extraídos.
# Os valores de 't' são armazenados em x_data
x_data = [trial.params['t'] for trial in trials]
# Frequências normalizadas são armazenadas em y_data.
y_data = [trial.histogram(key='m')[1] / 1000.0 for trial in trials]

# Gráfico de dispersão com 't' no eixo x e a frequência no eixo y.
# Os dados para o gráfico são fornecidos por {'t': x_data, 'p': y_data}.
plt.scatter('t', 'p', data={'t': x_data, 'p': y_data})

# É adicionado um rótulo para o eixo x e y usando plt.xlabel() e plt.ylabel().
plt.xlabel("trials")
plt.ylabel("frequency of qubit measured to be one")

# Gráfico é exibido
plt.show()
