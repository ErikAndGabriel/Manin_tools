from ui.banner import banner_execucao1 
from config.APIS.api_ip import APIS_IP
from core.config import timeout
from modulos.osint.formatters.formato import FORMATADORES
from modulos.osint.formatters.formate_api import format_ipwhois, format_ipapi, format_freeipapi, format_ip_api, format_ipinfo
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
          if self.api_ip in FORMATADORES:
            print(banner_execucao1)
            FORMATADORES[self.api_ip](data)
            return True
          else:
            return "erro de api invalida"  
        else:
          return "erro de conexão"
      except Exception as e:
        return f"erro: {e}"
