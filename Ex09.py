import numpy as np
import matplotlib.pyplot as plt

# Gerando os dados de chuva e colheita
desvio = np.random.random(size=100)

mm_chuva = np.arange(50, 150)
mm_chuva = mm_chuva * (desvio * 0.10)

colheita = np.arange(3, 103)
colheita = colheita * (desvio * 0.10)

# Função para calcular o custo (erro quadrático médio)
def calcular_custo(X, Y, B, W):
    Y_pred = B + W * X
    custo = np.mean((Y - Y_pred) ** 2)
    return custo

# Tentativas para encontrar os melhores valores de B e W
melhor_custo = float('inf')
melhor_B = None
melhor_W = None

# Tentativas
for _ in range(10):
    # Gerando valores aleatórios para B e W
    B = np.random.uniform(-10, 10)
    W = np.random.uniform(-1, 1)

    # Calculando o custo
    custo = calcular_custo(mm_chuva, colheita, B, W)

    # Verificando se este é o melhor custo
    if custo < melhor_custo:
        melhor_custo = custo
        melhor_B = B
        melhor_W = W

# Resultados
print(f'Melhor custo: {melhor_custo}')
print(f'Melhor B: {melhor_B}')
print(f'Melhor W: {melhor_W}')

# Plotando os dados e a linha de melhor ajuste
plt.scatter(mm_chuva, colheita, label='Dados')
Y_pred_final = melhor_B + melhor_W * mm_chuva
plt.plot(mm_chuva, Y_pred_final, color='red', label='Melhor ajuste')
plt.xlabel('Precipitação (mm)')
plt.ylabel('Colheita')
plt.legend()
plt.show()
