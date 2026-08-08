from ui.menus import menu_osint 
from ui.prompt import prompt_osint 
from ui.mensagens import erro, outro
from ui.banner import banner_execucao1 
from core.clear import clear
from modulos.osint.telegram_info_bot import BotTelegramInfo
from modulos.osint.telegram_info_chat import ChatTelegramInfo

def painel_telegram():
  while True:
    try:
      print(banner_execucao1)
      
