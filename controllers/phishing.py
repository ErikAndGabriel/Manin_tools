from ui.menus.menus import menu_phishing 
from ui.prompt import prompt_phishing
from ui.mensagens import erro
from core.carregar import carregar_json 
from core.clear import clear
def painel_phishing():
  while True:
    try:
      print(menu_phishing)
      ot = int(input(prompt_phishing))
      if ot == 0:
        clear()
        break
      else:
        erro("escolha invalida") 
        continue
    except ValueError:
      erro("somente numeros")
    except KeyboardInterrupt:
      exit()
    except Exception as e:
      erro(f"erro {e}")
