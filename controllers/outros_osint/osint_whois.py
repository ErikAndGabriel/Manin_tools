from ui.menus import menu_osint 
from ui.mensagens import erro, outro
from core.clear import clear
from modulos.osint.whois import BuscarWhois 

def painel_whois():
  while True:
    try:
      print(menu_osint)
      escolha = input("[0] sair or domain/ip > ")
      if escolha == "0":
        clear()
        break
      user = BuscarWhois(escolha)
      user.Buscar()
      outro()
      continue 
    except Exception as e:
      print(f"erro: {e}")
      outro
      continue
