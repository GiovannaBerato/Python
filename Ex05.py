import numpy as np

# 1. Importe a biblioteca NumPy e crie um array NumPy de números inteiros de 1 a 10.
inteiros = np.arange(1, 11)
print("Array de números inteiros: ", inteiros, "\n")

# 2. Crie um array Numpy de números float aleatórios entre 0 e 1 nas seguintes dimensões 300 x  200 x 3.
numeros_float = np.random.rand(300, 200, 3)
print("Array de números float aleatórios: ", numeros_float, "\n")

# 3. Crie um array de duas dimensões para guardar notas de alunos de uma disciplina, 
# sendo que existem 20 alunos na sala e cada aluno possuirá 3 notas na disciplina. 
# O array deverá conter números aleatórios inteiros entre 1 e 10 (inclusive).
notas = np.random.randint(1, 11, size=(20, 3))
for i in range(notas.shape[0]):
    print(f"Notas aluno {i + 1}: {notas[i]}")
print()

# 4. Crie um array NumPy com 12 elementos e o redimensione em uma matriz 3x4. Em seguida, realize a transposição dessa matriz.
elementos = np.arange(12)
print("Array com 12 elementos: ", elementos, "\n")

matriz = elementos.reshape(3, 4)
matriz_transposta = matriz.T

print("Matriz original:\n", matriz)
print("Matriz transposta:\n", matriz_transposta, "\n")

# 5. Crie dois arrays NumPy de mesma forma e realize as quatro operações aritméticas básicas (+, -, *, /) entre eles.
array1 = np.array([[2, 4, 6], [8, 10, 0]])
array2 = np.array([[1, 2, 3], [4, 5, 6]])

soma = array1 + array2
subtracao = array1 - array2
multiplicacao = array1 * array2
divisao = array1 / array2

print("Soma:\n", soma)
print("Subtração:\n", subtracao)
print("Multiplicação:\n", multiplicacao)
print("Divisão:\n", divisao, "\n")

# 6. Crie um array NumPy de números de 1 a 20 e, em seguida, imprima os elementos pares utilizando indexação e fatiamento.
numeros = np.arange(1, 21)
print("Array de números inteiros: ", numeros)

pares = numeros[numeros % 2 == 0]
print("Array de números pares: ", pares, "\n")

# 7. Crie um array NumPy de números aleatórios entre 1 e 100. Em seguida, selecione e exiba apenas os números maiores que 50.
aleatorios = np.random.randint(1, 101, size = 10) 

maiores_50 = aleatorios[aleatorios > 50]
print("Array de números aleatórios entre 1 e 100: ", aleatorios)
print("Array de números maiores que 50:", maiores_50, "\n")

# 8. Crie um array NumPy com 10 números aleatórios e calcule a média, mediana e desvio padrão desses números.
estatistica = np.random.randint(10, size = 10)  # Números aleatórios entre 0 e 1

media = np.mean(estatistica) 
mediana = np.median(estatistica) 
desvio_padrao = np.std(estatistica) 

print("Array de números aleatórios: ", estatistica)
print("Média:", media)
print("Mediana:", mediana)
print("Desvio padrão:", desvio_padrao)