from ui.menus.osint.whois import menu_whois
from ui.mensagens import erro, outro
from core.clear import clear
from modulos.osint.whois import BuscarWhois 
from ui.prompt.prompt_osint import prompt_whois
def painel_whois():
  while True:
    try:
      print(menu_whois)
      escolha = input(prompt_whois)
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
