import os
from ui.mensagens import erro, outro 
from ui.menus import menu_osint 
from ui.prompt import prompt_osint
from modulos.osint.email import Email 
def painel_email():
  while True:
    try:
      print(menu_osint)
      email = input("[0] sair or e-mail > ")
      if email == "0":
        clear()
        break
      user = Email(email)
      outros()
      continue
    except Exception as e:
      erro(f"erro: {e}")
      continue
