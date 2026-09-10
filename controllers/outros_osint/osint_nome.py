from ui.menus.osint.nome import menu_nome
from ui.prompt.prompt_osint import prompt_nome
from ui.mensagens import erro, outro
from core.clear import clear 
from modulos.osint.nome import NomeBusca

def painel_nome():
  while True:
    try:
      print(menu_nome)
      nome = input(f"nome or 0 {prompt_nome}")
      if nome == "0":
        clear()
        break 
      try:
        quantidade = int(input(f"quantidade {prompt_osint}"))
      except ValueError:
        erro("somente numeros")
        outro()
        
      user = NomeBusca(nome, quantidade)
      user.Buscar()
      outro()
    except Exception as e:
      erro(f"erro: {e}")
      outro()
