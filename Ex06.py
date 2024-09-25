import numpy as np

dados_meteorologicos = np.array([25, 26, 27, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12])

# Temperatura média anual
media = np.mean(dados_meteorologicos) 
print("Média da temperatura:", media)

# Temperatura máxima registrada
temp_max = np.max(dados_meteorologicos)
print("Temperatura máxima: ", temp_max)

# Temperatura mínima registrada
temp_min = np.min(dados_meteorologicos)
print("Temperatura mínima: ", temp_min)

# Desvio padrão da temperatura
desvio_padrao = np.std(dados_meteorologicos)
print("Desvio padrão da temperatura:", desvio_padrao)