import json

def carregar_wordlist(caminho):
  try:
    with open(f"{caminho}", "r") as arq:
      lista = []
      for linha in arq:
        lista.append(linha.strip())
      return lista
  except FileNotFoundError:
    return "erro, a worlist não foi encontrada"
  except Exception as e:
    return f"erro detectado: {e}"

def carregar_json(caminho):
  try:
    with open(f"{caminho}", "r") as arq:
      data = json.load(arq)
    return data
  except FileNotFoundError:
    return None
  except Exception as e:
    return None
