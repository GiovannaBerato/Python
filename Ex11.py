import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# 1. Carregar o arquivo e gerar listas
data = pd.read_csv('weatherAUS.csv')
X_min_temp = data['MinTemp'].dropna().tolist()
X_max_temp = data['MaxTemp'].dropna().tolist()
y_rain = (data['Rainfall'] > 0).astype(int).dropna().tolist()

# 2. Transformar listas em arrays do numpy
X = np.array(list(zip(X_min_temp, X_max_temp)))
y = np.array(y_rain)

# 3. Separar o conjunto de dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Criar o modelo de Regressão Logística
model = LogisticRegression()

# 5. Treinar o modelo
model.fit(X_train, y_train)

# 6. Verificar o Score do modelo
score = model.score(X_test, y_test)
print(f"Modelo Score: {score}")

# 7. Gerar valores para predição
predicted = model.predict(X_test)

# 8. Plotar o gráfico
plt.scatter(X_test[:, 0], predicted, color='blue', label='Previsão de Chuva')
plt.xlabel('Temperatura Mínima')
plt.ylabel('Previsão de Chuva')
plt.title('Predição de Chuva vs Temperatura Mínima')
plt.legend()
plt.show()
