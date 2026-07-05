def carregar_wordlist(wordlist):
  with open(f"../data/wordlist/{wordlist}", "r") as arq:
    lista = []
    for linha in arq:
      lista.append(linha.atrip())
    return lista
