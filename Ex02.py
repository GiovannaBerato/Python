def analisar_sentimentos(comentarios):
  """Analisa uma lista de comentários e retorna informações sobre os sentimentos.

  Args:
    comentarios: Uma lista de dicionários, onde cada dicionário representa um comentário.

  Returns:
    Um dicionário com as seguintes chaves:
      * 'total_positivos': Número total de comentários positivos.
      * 'total_negativos': Número total de comentários negativos.
      * 'proporcao_positivos': Proporção de comentários positivos.
      * 'proporcao_negativos': Proporção de comentários negativos.
      * 'comentarios_positivos': Lista de comentários positivos.
  """

  total_positivos = 0
  total_negativos = 0

  for comentario in comentarios:
    if comentario['Sentimento'] == 'Positivo':
      comentario['sentimento_valor'] = 1
      total_positivos += 1
    else:
      comentario['sentimento_valor'] = 0
      total_negativos += 1

  total_comentarios = total_positivos + total_negativos
  proporcao_positivos = total_positivos / total_comentarios
  proporcao_negativos = total_negativos / total_comentarios

  comentarios_positivos = [c for c in comentarios if c['sentimento_valor'] == 1]

  return {
      'total_positivos': total_positivos,
      'total_negativos': total_negativos,
      'proporcao_positivos': proporcao_positivos,
      'proporcao_negativos': proporcao_negativos,
      'comentarios_positivos': comentarios_positivos
  }

# Lista de comentários (dados do exemplo)
comentarios = [
  {'Autor': 'João', 'Comentário': 'Estou tão feliz hoje!', 'Sentimento': 'Positivo'},
  {'Autor': 'Maria', 'Comentário': 'Este filme é tão triste.', 'Sentimento': 'Negativo'},
  {'Autor': 'Carlos', 'Comentário': 'Que dia chuvoso entediante...', 'Sentimento': 'Positivo'},
  {'Autor': 'Ana', 'Comentário': 'Adorei a nova música da banda!', 'Sentimento': 'Negativo'},
  {'Autor': 'Roberto', 'Comentário': 'Eureka, consegui resolver este problema', 'Sentimento': 'Positivo'}
]

# Chamando a função e imprimindo os resultados
resultado = analisar_sentimentos(comentarios)
print("Total de comentários positivos:", resultado['total_positivos'])
print("Total de comentários negativos:", resultado['total_negativos'])
print("Proporção de comentários positivos:", resultado['proporcao_positivos'])
print("Proporção de comentários negativos:", resultado['proporcao_negativos'])
print("Comentários positivos:")
for comentario in resultado['comentarios_positivos']:
  print(f"Autor: {comentario['Autor']}, Comentário: {comentario['Comentário']}")