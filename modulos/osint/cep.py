import requests 
from config.APIS.api_cep import APIS_CEP
from core.config import timeout
class Cep:
  def __init__(self, cep, api):
    
    self.cep = cep
    self.api = api
    self.timeout = timeout("api")
    
  def CepBusca(self):
    url = APIS_CEP[self.api]["url"]
    try:
      resposta = requests.get(
        url,
        timeout=self.timeout
      )
      if resposta.status_code == 200:
        data = resposta.json()
        for chave, valor in data.items():
          print(f"{chave} : {valor}")
        return True
      else:
        return "erro resposta"
    except Exception as e:
      return f"erro: {e}"
