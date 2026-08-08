from ui.menus import menu_telegram
from ui.prompt import prompt_osint 
from ui.mensagens import erro, outro
from core.clear import clear
from modulos.osint.telegram_info_bot import BotTelegramInfo
from modulos.osint.telegram_info_chat import ChatTelegramInfo

def painel_telegram():
  while True:
    try:
      print(menu_telegram)     
