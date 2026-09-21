import requests
from config.sites import SITES
from ui.mensagens import outro, erro, erro_loop, sucesso_loop
from ui.banner import banner_execucao1
from core.config import timeout
class UserName:
    def __init__(self, user_name):
       self.user_name = user_name
       self.timeout = timeout("Google")
    def buscar(self):
       try:
          print(banner_execucao1)
          for site, url in SITES.items():
              try:
                 url_final = url.format(self.user_name)
                 resposta = requests.get(url_final, timeout=self.timeout)
                 if resposta.status_code == 200:
                    sucesso_loop(f"{site} : {url_final}")
                 else:
                    erro_loop(f"{site} : {url_final}")
              except KayboardInterrupt:
                 outro()
              except:
                 erro_loop(f"{site} : {url_final}")
       except Exception as error:
          erro(f"error: {error}")
          return False
       except KayboardInterrupt:
          outro()

u = UserName("erikmxp")
u.buscar()
