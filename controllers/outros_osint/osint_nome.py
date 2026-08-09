from ui.menus import menu_osint
from ui.prompt import prompt_osint 
from ui.mensagens import erro, outro
from core.clear import clear 
from modulos.osint.nome import NomeBusca

def painel_nome():
  while True:
    try:
      print(menu_osint)
      nome = input(f"nome or 0 {menu_osint}")
      if nome == "0":
        clear()
        break
        
      user = NomeBusca(nome)
      user.Buscar()
      outro()
    except Exception as e:
      erro(f"erro: {e}")
      outro()
