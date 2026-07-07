from ui.menus import menu_principal
from ui.prompt import prompt_menu
from ui.mensagens import erro
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
      else:
        erro("escolha invalida")
        continue 
    except ValueError:
      erro("erro, somente numeros")
      continue
