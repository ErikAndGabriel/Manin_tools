from ui.banner import banner_execucao1 
from config.APIS.api_bin import APIS_BIN
from core.config import timeout
from modulos.osint.formatters.formato import FORMATADORES_BIN
from core.clear import clear
from modulos.osint.formatters.formate_api import format_ipwhois, format_ipapi, format_freeipapi, format_ip_api, format_ipinfo
import json 
import requests 

class Bin:
  def __init__(self, bin, api):
    self.bin = bin
    self.api_bin = api
    self.timeout = timeout("api")
    
  def BinBusca(self):
    if self.api_bin in APIS_BIN:
      url = APIS_IP[self.api_bin]["url"].format(self.bin)
      try:
        resposta = requests.get(
          url, 
          timeout=self.timeout
        )
        if resposta.status_code == 200:
          data = resposta.json()
          if self.api_bin in FORMATADORES_BIN:
            clear()
            print(banner_execucao1)
            FORMATADORES_BIN[self.api_bin](data)
            return True
          else:
            return "erro de api invalida"  
        else:
          return "erro de conexão"
      except Exception as e:
        return f"erro: {e}"
