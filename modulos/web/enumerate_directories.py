import requests
from core.carregar import carregar_wordlist
from ui.mensagens import erro, sucesso, mensagem

wordlist = "diretórios.txt"

class EnumerateDirectori:
  def __init__(self, url,):
    self.url = url
    self.wordlist = carregar_wordlist(wordlist)
    self.numero_sucesso = 0
    self.numero_erro = 0
    self.enumerar_sucesso = 1
    self.enumerar_erro = 1
    self.sucesso = []
    self.erro = []
    
  def Scan(self):
    print(f"""
    site : {self.url}
    wordlist : data/wordlist/{wordlist}
    requests : get
    """

    for diretorios in self.wordlist:
      url = f"{self.url}{diretorios}"
      mensagem(f"testando : {url}")
      resposta = requests.get(url) 
      if resposta.status_code == 200:
        sucesso(f"sucesso : {self.url}{diretorios}")
        self.sucesso.append(url)
        self.numero_sucesso += 1

      else:
        self.erro.append(url)
        self.numero_erro += 1
    
  def Relatorio(self):
    
    print(f"""
    ========== RELATORIO ==========
    site............: {self.url}
    wordlist........: data/wordlist/{wordlist}
    método..........: Get
    total tentativas: {self.numero_sucesso + self.numero_erro}
    encontrado......: {self.numero_sucesso}
    não encontrado..: {self.numero_erro}
    resposta sucesso: 200
    resposta erro...: 404
    """
    print("")
    sucesso(10 * "=", "[200]", 10 * "=") 
    for url in self.sucesso:
      sucesso(f"{self.enumerar_sucesso} sucesso: {url}")
      self.enumerar_sucesso += 1
    erro(10 * "=", "404", 10 * "=")
    for url in self.erro:
      erro(f"{self.enumerar_erro} erro: {url}")
      self.enumerar_erro += 1

   
      

    

  
