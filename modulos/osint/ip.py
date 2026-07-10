from config.APIS.api_ip import APIS_IP
from core.config import timeout
import json 
import requests 

class Ip:
  def __init__(self, ip, api):
    self.ip = ip
    self.api_ip = api
    self.timeout = timeout("api")
    
  def IpBusca(self):
    if self.api_ip in APIS_IP:
      url = APIS_IP[self.api_ip]["url"].format(self.ip)
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
          return "erro de conexão"
      except Exception as e:
        return f"erro: {e}"
