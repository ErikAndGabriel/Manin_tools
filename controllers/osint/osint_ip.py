from ui.menu import menu_ip
from ui.prompt import prompt_osint
from ui.mensagens import erro
from modulos.osint.ip import Ip
from core.clear import clear

def painel_ip():
  while True:
    try:
      print(menu_ip)
      ot = int(input(prompt_ip))
      if ot == 0:
        clear()
        break
      else:
        erro("escolha invalida")
        continue
    except ValueError:
      erro("somente numeros")
      continue
    except Exception as e:
      erro(f"erro: {e}")
