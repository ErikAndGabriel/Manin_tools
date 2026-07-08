from ui.menus import menu_phishing 
from ui.prompt import prompt_phishing
from ui.mensagens import erro
from core.carregar import carregar_json 

def painel_phishing():
  while True:
    try:
      print(menu_phishing)
      ot = int(input(prompt_phishing))
    except ValueError:
      erro("somente numeros")
    except Exception as e:
      erro(f"erro {e}")
