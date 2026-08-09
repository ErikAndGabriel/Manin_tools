from googlesearch import search, get_useragent
from core.clear import clear 
from ui.banner import banner_execucao1
from core.config import timeout, headers
class NomeBusca:
  def __init__(self, nome, quantidade):
    self.nome = nome
    self.quantidade = quantidade
    self.timeout = timeout("Google")
    self.user_agente = headers("aleatorio")
    self.enumerar = 0
  def Buscar(self):
    for resultado in search(self.nome,
                      advanced=True,
                      num_results=self.quantidade,
                      sleep_interval=2):
        print(f"============ {self.enumerar} =========")
        print(f"url.      : {resultado.url}")
        print(f"titulo.   : {resultado.title}")
        print(f"descrição : {resultado.description}")
        
