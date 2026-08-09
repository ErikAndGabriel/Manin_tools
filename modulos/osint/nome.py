from googlesearch import search, get_useragent
from core.clear import clear 
from ui.banner import banner_execucao1
from core.config import timeout, headers
from ui.mensagens import erro 
class NomeBusca:
  def __init__(self, nome, quantidade):
    self.nome = nome
    self.quantidade = quantidade
    self.timeout = timeout("Google")
    self.enumerar = {
      "erro": 0,
      "sucesso": 0
    }
  def Buscar(self):
    clear()
    print(banner_execucao1)
    try:
      for resultado in search(self.nome,
                        advanced=True,
                        num_results=self.quantidade,
                        sleep_interval=self.timeout):
          print()
          print(f"url.      : {resultado.url}")
          print(f"titulo.   : {resultado.title}")
          print(f"descrição : {resultado.description}")
          self.enumerar["sucesso"] += 1
      print(f"quantidade : {self.quantidade}")
      print(f"sucesso.   : {self.sucesso}")
      print(f"erro.      : {self.erro}")
      self.enumerar["sucesso"] = 0
      self.enumerar["erro"] = 0
    except Exception as e:
      erro(f"erro: {e}")
      self.enumerar["erro"] += 1      
#tão tedioso, igual a sua vida 
