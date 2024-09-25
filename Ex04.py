import re

# Dicionário de correção de abreviações e erros comuns
correcoes = {
    "vc": "você",
    "vcs": "vocês",
    "eh": "é",
    "q": "que",
    "tb": "também",
    "pq": "porque",
    "blz": "beleza",
    "msg": "mensagem",
    "nao": "não",
    "n": "não",
    "tá": "está",
    "ta": "está",
    "obg": "obrigado",
    "vlw": "valeu",
    "dps": "depois",
    "blz": "beleza"
}

# Lista de gírias ou expressões a serem removidas
girias = ["tipo", "mano", "véi", "pô", "aff", "mó", "aí", "então"]

def normalizar_texto(texto):
    # Corrigir abreviações e erros comuns
    palavras = texto.split()
    palavras_normalizadas = []
    
    for palavra in palavras:
        palavra_limpa = re.sub(r'[^\w\s]', '', palavra.lower())  # Remove pontuações
        if palavra_limpa in correcoes:
            palavra_normalizada = correcoes[palavra_limpa]
        elif palavra_limpa not in girias:
            palavra_normalizada = palavra
        else:
            palavra_normalizada = ''
        
        if palavra_normalizada:
            palavras_normalizadas.append(palavra_normalizada)

    # Juntar as palavras normalizadas e retornar o texto corrigido
    return ' '.join(palavras_normalizadas)

# Exemplo de uso
texto_informal = "vc pode me mandar a msg dps? vlw mano!"
texto_normalizado = normalizar_texto(texto_informal)
print(texto_normalizado)

