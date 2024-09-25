import numpy as np

# Função que calcula a pontuação final dos alunos
def calcular_pontuacao(matriz_notas, pesos):
    # Multiplica as notas pelos pesos e retorna a soma ponderada de cada aluno
    return np.dot(matriz_notas, pesos)

# Função principal
def main():
    # Pedir a quantidade de alunos
    num_alunos = int(input("Quantos alunos serão avaliados? "))
    
    # Pedir a quantidade de seções
    num_secoes = int(input("Quantas seções existem na avaliação? "))
    
    # Pedir os pesos de cada seção e armazenar em uma lista
    pesos = []
    for i in range(num_secoes):
        peso = float(input(f"Informe o peso da seção {i+1}: "))
        pesos.append(peso)
    
    # Converter a lista de pesos para um array numpy
    pesos = np.array(pesos)
    
    # Verificar se a soma dos pesos é igual a 10
    if np.sum(pesos) != 10.0:
        print("A soma dos pesos não é igual a 10. Tente novamente.")
        return
    
    # Criar uma matriz para armazenar as notas de cada aluno
    matriz_notas = []
    
    # Pedir as notas de cada aluno
    for i in range(num_alunos):
        notas_aluno = []
        for j in range(num_secoes):
            nota = float(input(f"Informe a nota da seção {j+1} para o aluno {i+1}: "))
            notas_aluno.append(nota)
        matriz_notas.append(notas_aluno)
    
    # Converter a lista de notas para um array numpy
    matriz_notas = np.array(matriz_notas)
    
    # Calcular a pontuação final de cada aluno
    pontuacoes_finais = calcular_pontuacao(matriz_notas, pesos)
    
    # Exibir as pontuações finais de cada aluno
    for i in range(num_alunos):
        print(f"A pontuação final do aluno {i+1} é: {pontuacoes_finais[i]}")

# Executar o programa principal
if __name__ == "__main__":
    main()
