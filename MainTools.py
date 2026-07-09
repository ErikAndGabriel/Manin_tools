from ui.menus import menu_principal
from ui.prompt import prompt_menu
from ui.mensagens import erro
from core.clear import clear
from controllers.osint import painel_osint
from controllers.phishing import painel_phishing
from controllers.web import painel_web
from controllers.network import painel_network
from controllers.malware import painel_malware
from controllers.loorkup import painel_lorkup
from config.ferramentas.menu_principal import opcoes


def inicial():
  while True:
    try:
      print(menu_principal)
      ot = int(input(prompt_menu))
      if ot == 0:
        break
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
