import json

def carregar_wordlist(wordlist):
  try:
    with open(f"{wordlist}", "r") as arq:
      lista = []
      for linha in arq:
        lista.append(linha.strip())
      return lista
  except FileNotFoundError:
    return "erro, a worlist não foi encontrada"
  except Exception as e:
    return f"erro detectado: {e}"

def carregar_json(json):
  try:
    with open(f"{json}", "r") as arq:
      data = json.load(arq)
    return data
  except FileNotFoundError:
    return "erro, o json não foi encontrado"
  except Exception as e:
    return f"erro detectado: {e}"
