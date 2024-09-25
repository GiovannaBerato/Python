import pandas as pd

# Carregar o arquivo CSV
data = pd.read_csv('weatherAUS.csv')

# Gerar listas
temperatura_minima = data['TempMin'].tolist()
temperatura_maxima = data['TempMax'].tolist()
rainfall = data['Rainfall'].tolist()

import numpy as np

# Transformar listas em arrays
X = np.array(list(zip(temperatura_minima, temperatura_maxima)))
y = np.array([1 if x > 0 else 0 for x in rainfall])  # 1 para chuva, 0 para não chuva

from sklearn.model_selection import train_test_split

# Separar os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

from sklearn.linear_model import LogisticRegression

# Criar o modelo
model = LogisticRegression()

# Treinar o modelo
model.fit(X_train, y_train)

# Verificar o score
score = model.score(X_test, y_test)
print(f'Score do modelo: {score:.2f}')

# Gerar algumas previsões
valores_predicao = np.array([[15, 25], [10, 30], [20, 22]])  # Exemplo de temperatura mínima e máxima
predicoes = model.predict(valores_predicao)
print(f'Predições: {predicoes}')

import matplotlib.pyplot as plt

# Prever com os dados de teste
y_pred = model.predict(X_test)

# Plotar
plt.figure(figsize=(10, 6))
plt.scatter(X_test[:, 0], y_pred, alpha=0.5)
plt.title('Predição de Chuva com base na Temperatura Mínima')
plt.xlabel('Temperatura Mínima (°C)')
plt.ylabel('Predição (1: Chuva, 0: Sem Chuva)')
plt.axhline(0.5, color='red', linestyle='--')  # Linha de decisão
plt.show()
