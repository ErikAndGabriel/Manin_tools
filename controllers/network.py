from ui.menus import menu_network
from ui.mensagens import erro
from ui.prompt import prompt_network
from core.clear import clear
def painel_network():
  while True:
    try:
      print(menu_network)
      ot = int(input(prompt_network))
      if ot == 0:
        clear()
        break
    except ValueError:
      erro("somente numeros")
    except KeyboardInterrupt:
      exit()
    except Exception as e:
      erro(f"erro: {e}")
