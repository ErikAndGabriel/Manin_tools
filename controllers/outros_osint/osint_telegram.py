from ui.menus import menu_telegram
from ui.prompt import prompt_telegram 
from ui.mensagens import erro, outro
from core.clear import clear 
from modulos.osint.telegram_info_bot import BotTelegramInfo
from modulos.osint.telegram_info_chat import ChatTelegramInfo

def painel_telegram():
  while True:
    try:
      print(menu_telegram) 
      escolha = int(input(prompt_telegram))
      if escolha == 1:
        chat_id = input(f"chat id {prompt_telegram}")
        bot_token = input(f"bot token {prompt_telegram}")
        user = ChatTelegramInfo(bot_token, chat_id)
        user.Buscar()
        outro()
      elif escolha == 0:
        clear()
        break
        
      elif escolha == 2:
        bot_token = input(f"bot token {prompt_telegram}")
        user = BotTelegramInfo(bot_token)
        user.Buscar()
        outro()
        
      else:
        erro("escolha invalida")
        outro()
    except ValueError:
      erro("somente numeros")
      outro()
    except KeyboardInterrupt:
      break
    except Exception as e:
      erro(f"erro: {e}")
