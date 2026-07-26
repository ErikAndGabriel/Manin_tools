import os
from ui.mensagens import erro, outro 
from ui.menus import menu_osint 
from ui.prompt import prompt_osint
from modulos.osint.email import Email 
def painel_email():
  while True:
    try:
      print(menu_osint)
      e-mail = input("e-mail > ")
      user = Email(e-mail)
    except Exception as e:
      erro(f"erro: {e}")
