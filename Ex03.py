import re

def preprocessar_texto(texto):
  """
  Pré-processa um texto, convertendo para minúsculas e removendo caracteres especiais.

  Args:
    texto: Uma string de texto.

  Returns:
    Uma lista de palavras pré-processadas.
  """

  # Converter para minúsculas
  texto = texto.lower()

  # Remover caracteres especiais (pode ser ajustado para diferentes casos)
  texto = re.sub(r'[^\w\s]', '', texto)

  # Tokenizar (separar em palavras)
  palavras = texto.split()

  return palavras

# Exemplo de uso:
comentario = "Este é um #teste com muitos caracteres especiais! "
palavras_processadas = preprocessar_texto(comentario)
print(palavras_processadas)  # Saída: ['este', 'é', 'um', 'teste', 'com', 'muitos', 'caracteres', 'especiais']