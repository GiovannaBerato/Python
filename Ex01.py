def extrair_texto_entre_ponto_e_virgula(texto):
    posicao_ponto = texto.find(".")
    if posicao_ponto == -1:
        return "Ponto não encontrado."

    posicao_virgula = texto[posicao_ponto+1:].find(",") + posicao_ponto + 1
    if posicao_virgula == posicao_ponto:
        return "Vírgula não encontrada após o ponto."

    return texto[posicao_ponto+1:posicao_virgula]

texto = """
Python é uma linguagem de programação poderosa e versátil.
É amplamente utilizada em desenvolvimento web, ciência de dados, 
inteligência artificial e muito mais.
"""

resultado = extrair_texto_entre_ponto_e_virgula(texto)
print(resultado)