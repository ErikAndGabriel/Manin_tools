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
      escolha = int(input(prompt_email))
      if escolha == 0:
        clear()
        break
      elif escolha == 1:
        email = input(f"email {prompt_email}")
        user = Email(email)
        outro()
        continue
      else:
        erro("escolha invalida")
        outro()
        continue
    except Exception as e:
      erro(f"erro: {e}")
      continue
    except ValueError:
      erro("somente numeros!")
      outro()
      continue
