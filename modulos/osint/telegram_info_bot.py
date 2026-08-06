from config.APIS.api_telegram import APIS_TELEGRAM
from modulos.osint.formatters.formate_api import 
import requests 
import json

class BotTelegramInfo:
  def __init__(self, token_bot):
    self.token_bot = token_bot

  def Buscar(self):
    data = {}
    for nome, url in APIS_TELEGRAM["info_bot"].items():
      try:
        resposta = requests.get(
          url.format(self.token_bot)
        )
        data[nome] = resposta.json()
        
      except Exception as e:
        data[nome] = {
          "ok": False,
          "erro": str(e)
        }
    
