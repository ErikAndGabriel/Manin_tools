import requests 
from config.APIS.api_cep import APIS_CEP
from core.config import timeout
from modulos.osint.formatters.formato import FORMATADORES_CEP
class Cep:
  def __init__(self, cep, api):
    
    self.cep = cep
    self.api = api
    self.timeout = timeout("api")
    
  def CepBusca(self):
    url = APIS_CEP[self.api]["url"].format(self.cep)
    try:
      resposta = requests.get(
        url,
        timeout=self.timeout
      )
      if resposta.status_code == 200:
        data = resposta.json()
        if self.api in FORMATADORES_CEP:
          FORMATADORES_CEP[self.api](data)
        return True
      else:
        return "erro resposta"
    except Exception as e:
      return f"erro: {e}"
