from modulos.osint.cpf import SisregConsulta
from ui.menus.osint.cpf import menu_cpf 
from ui.prompt import prompt_osint 
from ui.mensagens import erro, outro
from ui.banner import banner_execucao1 
from core.clear import clear
def painel_cpf():
  while True:
    try:
      print(menu_osint)
      cpf = input("[0] sair or cpf > ")
      if cpf == "0":
        clear()
        break
      clear()
      print(banner_execucao1)
      usuario = SisregConsulta(cpf)
      outro()
      continue
    except Exception as e:
      erro(f"erro: {e}")
      continue
      
