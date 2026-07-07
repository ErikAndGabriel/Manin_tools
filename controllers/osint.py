from ui.menus import menu_osint
from ui.prompt import prompt_osint
from ui.mensagens import erro
from modulos.osint.ip import Ip

def painel_osint():
  while True:
    try:
      print(menu_osint)
      ot = int(input(prompt_osint))
    except ValueError:
      erro("erro, somente numeros")
      
