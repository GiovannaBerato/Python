import pandas as pd

# Carregue o arquivo
df = pd.read_csv('population.csv')

# Gere listas com anos e população urbana
anos = df['Year'].tolist()
populacao_urbana = df['Urban Population'].tolist()

import numpy as np

# Converta listas em arrays do numpy
x = np.array(anos)
y = np.array(populacao_urbana)

def funcao_linear(x, w, b):
    return w * x + b

# Inicializar w e b
w = 0.0
b = 0.0

# Calcular y_hat
y_hat = funcao_linear(x, w, b)

import matplotlib.pyplot as plt

plt.scatter(x, y, color='blue', label='Dados Reais')
plt.plot(x, y_hat, color='red', label='Modelo Inicial')
plt.xlabel('Ano')
plt.ylabel('População Urbana')
plt.title('População Urbana na Índia')
plt.legend()
plt.show()

def custo(y, y_hat):
    m = len(y)
    return np.sum((y_hat - y) ** 2) / (2 * m)


### 8. Função para novo `w`

def novo_w(w, x, y, y_hat, learn_rate):
    m = len(y)
    return w - learn_rate * np.sum((y_hat - y) * x) / m

def novo_b(b, x, y, y_hat, learn_rate):
    m = len(y)
    return b - learn_rate * np.sum(y_hat - y) / m

# Definir a taxa de aprendizado e número de iterações
learn_rate = 0.0001
num_iteracoes = 30

for i in range(num_iteracoes):
    y_hat = funcao_linear(x, w, b)  # Calculo do y_hat
    custo_atual = custo(y, y_hat)  # Custo atual
    w = novo_w(w, x, y, y_hat, learn_rate)  # Novo valor de W
    b = novo_b(b, x, y, y_hat, learn_rate)  # Novo valor de B

    print(f'Iteração {i + 1}: w = {w}, b = {b}, custo = {custo_atual}')

# Calcular y_hat com os valores otimizados
y_hat = funcao_linear(x, w, b)

plt.scatter(x, y, color='blue', label='Dados Reais')
plt.plot(x, y_hat, color='red', label='Modelo Otimizado')
plt.xlabel('Ano')
plt.ylabel('População Urbana')
plt.title('População Urbana na Índia - Modelo Otimizado')
plt.legend()
plt.show()
