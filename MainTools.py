from ui.menus import menu_principal
from ui.prompt import prompt_menu

opcoes = {
  "1": "phishing",
  "2": "osint"
}

def inicial():
  while True:
    try:
      print(menu_principal)
      ot = int(input(prompt_menu)
      for escolha in opcoes.values():
        if ot == opcoes[str(ot)]:
               opcoes[str(ot)]()
