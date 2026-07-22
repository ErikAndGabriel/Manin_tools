from modulos.osint.cpf import SisregConsulta
from ui.menus import menu_osint 
from ui.prompt import prompt_osint 
from ui.mensagens import erro
def painel_cpf():
  while True:
    try:
      print(menu_osint)
      cpf = input(prompt_osint)
      usuario = SisregConsulta(cpf)
    except Exception as e:
      erro(f"erro: {e}")
      continue
      
