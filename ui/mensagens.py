from ui.color import vermelho, verde, amarelo, roxo 

def erro(data):
  print(vermelho, data)

def sucesso(data):
  print(verde, data)

def mensagem(data):
  print(amarelo, data)

def personalizar(data, color_tipo):
  print(color_tipo, data)
