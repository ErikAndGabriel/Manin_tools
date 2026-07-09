from ui.menus import menu_lookup
from ui.mensagens import erro
from ui.prompt import prompt_lorkup 
from core.carregar import carregar_json 
from core.clear import clear

def painel_lorkup():
  while True:
    try:
      print(menu_lorkup)
      ot = int(input(prompt_lorkup))
      if ot == 0:
        clear()
        break
    except ValueError:
      erro("somente numeros")
    except KeyboardInterrupt:
      break
    except Exception as e:
      erro(f"erro: {e}")
