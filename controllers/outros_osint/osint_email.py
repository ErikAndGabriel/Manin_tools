import os
from core.clear import clear
from ui.mensagens import erro, outro 
from ui.menus.osint.email import menu_email
from ui.prompt.prompt_osint import prompt_email
from modulos.osint.email import Email 
def painel_email():
  while True:
    try:
      print(menu_email)
      email = input(prompt_email)
      if email == "0":
        clear()
        break
      user = Email(email)
      outro()
      continue
    except Exception as e:
      erro(f"erro: {e}")
      continue
