from ui.menus import menu_osint
from ui.prompt import prompt_osint 
from ui.mensagens import erro, outro
from core.clear import clear 
from modulos.osint.nome import NomeBusca

def painel_nome():
  while True:
    try:
      print(menu_osint)
      nome = input(f"nome or 0 {prompt_osint}")
      try:
        quantidade = int(input(f"quantidade or 0 {prompt_osint}"))
      except ValueError:
        erro("somente numeros")
        outro()
      if nome == "0":
        clear()
        break
        
      user = NomeBusca(nome, quantidade)
      user.Buscar()
      outro()
    except Exception as e:
      erro(f"erro: {e}")
      outro()
