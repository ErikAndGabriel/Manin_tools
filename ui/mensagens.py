from ui.color import vermelho, verde, amarelo, roxo 

def global():
  input("precione [ENTER]")
  
def erro(data):
  print(vermelho, data)
  global()
  
def sucesso(data):
  print(verde, data)
  global()
  
def mensagem(data):
  print(amarelo, data)
  
def personalizar(data):
  print(roxo, data)
  global()
