import whois
from ui.menus import menu_osint 
from ui.banner import banner_execucao1 
from core.clear import clear 

class BuscarWhois:
  def __init__(self, servico):
    self.servico = servico
    
  def Buscar(self):
    try:
      clear()
      print(banner_execucao1)
      buscar = whois.whois(self.servico)
      for chave, valor in buscar.items():
        print(f"{chave} : {valor}")
        return True
    except Exception as e:
      return f"erro {e}"
