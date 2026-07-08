from ui.menus import menu_network
from ui.mensagens import erro
from ui.prompt import prompt_network

def painel_network():
  while True:
    try:
      print(menu_network)
      ot = int(input(prompt_network)
    except ValueError:
      erro("somente numeros")
    except Exception as e:
      erro(f"erro: {e}")
