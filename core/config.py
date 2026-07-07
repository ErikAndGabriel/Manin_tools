from core.carregar import carregar_json 
import random 
def timeout(tempo=5):
  if tipo == "api":
    return 5
  elif tipo == "scaner":
    return 10
  elif tipo == "resposta":
    return 20

def headers(tipo="aleatorio"):
  data = carregar_json("config/user_agents.json")
  user_agentes = data["user_agents"]
  if tipo == "aleatorio":
    aleatorio = []
    for header in user_agentes.values():
       aleatorio.extend(header)
    user_agente = random.choice(aleatorio)
    return user_agente
    
  elif tipo == "android":
    android = []
    for header in user_agentes.values():
      if tipo == header["tipo"]:
        android.extend(headers)
    user_agente = random.choice(android)
    return user_agente
    
  elif tipo == "desktop":
    desktop = []
    for header in user_agentes.values():
      if tipo == header["tipo"]:
        desktop.extend(headers)
    user_agente = random.choice(desktop)
    return user_agente

  
