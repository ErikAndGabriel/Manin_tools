from ui.menus.menus import menu_web
from ui.prompt import prompt_web
from ui.mensagens import erro
from core.carregar import carregar_json 
from core.clear import clear

def painel_web():
  while True:
    try:
      print(menu_web)
      ot = int(input(prompt_web))
      if ot == 0:
        clear()
        break
      else:
        erro("escolha invalida")
        continue
    except ValueError:
      erro("somente numeros")
      continue
    except KeyboardInterrupt:
      exit()
    except Exception as e:
      erro(f"erro: {e}")
      continue
      
