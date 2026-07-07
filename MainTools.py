from ui.menus import menu_principal
from ui.prompt import prompt_menu
from ui.mensagens import erro
from core.clear import clear
from controllers.osint import painel_osint 
opcoes = {
  "1": "phishing",
  "2": painel_osint
}

def inicial():
  while True:
    try:
      print(menu_principal)
      ot = int(input(prompt_menu))
      if str(ot) in opcoes:
        clear()
        opcoes[str(ot)]()
        
      else:
        erro("escolha invalida")
        continue 
    except ValueError:
      erro("erro, somente numeros")
      continue
    except Exception as e:
      erro(f"erro: {e}") 

if __name__ == "__main__":
  clear()
  inicial()
