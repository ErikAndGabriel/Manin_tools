from ui.menus import menu_principal
from ui.prompt import prompt_menu
from ui.mensagens import erro
from core.clear import clear
from core.carregar import carregar_json 
from controllers.osint import painel_osint
from controllers.phishing import painel_phishing
from controllers.web import painel_web
from controllers.network import painel_network
from controllers.malware import painel_malware
from controllers.loorkup import painel_lorkup

caminho = "config/ferramentas/menu_principal.json"
opcoes = carregar_json(caminho)

def inicial():
  while True:
    try:
      print(menu_principal)
      ot = int(input(prompt_menu))
      if str(ot) in opcoes:
        clear()
 
        opcoes[str(ot)]()
      elif ot == 0:
        break
        
      else:
        erro("escolha invalida")
        continue
      if opcoes in None:
        erro("arquivo nao encontrado")
        continue 
        
    except ValueError:
      erro("erro, somente numeros")
      continue
    except Exception as e:
      erro(f"erro: {e}") 

if __name__ == "__main__":
  clear()
  inicial()
