from config.APIS.api_telegram import APIS_TELEGRAM
from modulos.osint.formatters.formate_api import format_telegram_info_chat
from ui.banner import banner_execucao1 
from core.config import timeout
from core.clear import clear 
import requests 
import json

class ChatTelegramInfo:
  def __init__(self, token_bot, chat_id):
    self.token_bot = token_bot
    self.chat_id = chat_id
    self.timeout = timeout("api")
  def Buscar(self):
    data = {}
    for nome, url in APIS_TELEGRAM["info_chat"].items():
      try:
        resposta = requests.get(
          url.format(self.token_bot).format(self.chat_id), 
          timeout=self.timeout 
        )
        if resposta.status_code == 200:
          data[nome] = resposta.json()
        else:
          data[nome] = {
            "ok": False,
            "erro": str(resposta.status_code)
          }
      except Exception as e:
        data[nome] = {
          "ok": False,
          "erro": str(e)
        }
    clear()
    print(banner_execucao1)
    format_telegram_info_chat(data)
