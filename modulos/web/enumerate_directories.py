import requests
from core.carregar import carregar_wordlist
from core.carregar import carregar_json
from ui.mensagens import erro, sucesso, mensagem, personalizar

json_resposta = "config/respostas_web.json"
json_app = "config/app.json"
wordlist = "data/wordlist/diretórios.txt"

class EnumerateDirectori:
  def __init__(self, url,):
    self.url = url
    self.wordlist = carregar_wordlist(wordlist)
    self.resposta = carregar_json(json_resposta)
    self.app = carregar_json(json_app)
    self.sucesso = 0
    self.erro = 0
    
  def Scan(self):
    print(f"""
    site : {self.url}
    wordlist : {wordlist}
    requests : get
    """)

    for diretorios in self.wordlist:
      url = f"{self.url}{diretorios}"
      mensagem(f"testando : {url}")
      resposta = requests.get(url) 
      status = str(resposta.status_code)
      
      if status in self.resposta["respostas"]["sucesso"]:
        sucesso(f"{url} ---> {status}")
        self.sucesso +=1
      
      elif status in self.resposta["respostas"]["protegido"]:
        personalizar(f"{url} ---> {status}")
        self.sucesso += 1
      
      elif status in self.resposta["respostas"]["redirecionamento"]:
        sucesso(f"{url} ---> {status}")
        self.sucesso += 1
        
      elif status in self.resposta["respostas"]["erro"]:
        self.erro += 1

      else:
        print("erro inesperado")
    
  def Relatorio(self):
    
    print(f"""
    ========== RELATORIO ==========
    site............: {self.url}
    wordlist........: {wordlist}
    método..........: Get
    total tentativas: {self.sucesso + self.erro}
    encontrado......: {self.sucesso}
    não encontrado..: {self.erro}
    resposta sucesso: 200
    resposta erro...: 404
    ========== CREDITOSS ==========
    nome............: {self.app["nome"]}
    github..........: {self.app["git"]}
    versão..........: {self.app["version"]}
    e-mail..........: {self.app["email"]}
    mensagem........: {self.app["mensagem"]}
    ===============================
    """)
