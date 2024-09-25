import numpy as np

# Dados de altura e peso
altura = np.array([1.65, 1.75, 1.80, 1.70, 1.68, 1.72, 1.78, 1.60, 1.85, 1.73, 1.69, 1.75, 1.62, 1.80, 1.77, 1.68, 1.79, 1.81, 1.76, 1.74])
peso = np.array([65, 70, 75, 80, 60, 68, 72, 58, 90, 72, 65, 70, 55, 78, 79, 62, 85, 88, 70, 75])

# Calculando o IMC
imc = peso / (altura ** 2)

# Categorias de IMC
abaixo_peso = np.sum(imc < 18.5)
peso_normal = np.sum((imc >= 18.5) & (imc < 24.9))
sobrepeso = np.sum((imc >= 24.9) & (imc < 29.9))
obesidade = np.sum(imc >= 30)

# Exibindo os resultados
print("IMC calculado para cada pessoa: ", imc)
print(f"Pessoas abaixo do peso: {abaixo_peso}")
print(f"Pessoas com peso normal: {peso_normal}")
print(f"Pessoas com sobrepeso: {sobrepeso}")
print(f"Pessoas obesas: {obesidade}")
