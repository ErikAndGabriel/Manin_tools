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
    url = self.api_ip.format(self.ip)
    resposta = requests.get(
      url, 
      timeout=self.timeout
    )
    
    if resposta.status_code == 200:
      for chave, valor in resposta.values():
        print(f"{chave} : {valor}")
      return True
    else:
      return "erro de conexão"
