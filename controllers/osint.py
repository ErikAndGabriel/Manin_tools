from ui.menus import menu_osint
from ui.prompt import prompt_osint
from ui.mensagens import erro
from config.ferramentas.osint import ferramentas 
from core.clear import clear
from controllers.outros_osint.osint_ip import painel_ip

def painel_osint():
  while True:
    try:
      print(menu_osint)
      ot = int(input(prompt_osint))
      if ot == 0:
        clear()
        break
        
      if str(ot) in ferramentas:
        clear()
        ferramentas[str(ot)]()
          
      else:
        erro("somente numeros")
        continue
    except ValueError:
      erro("erro, somente numeros")
      continue
    except KeyboardInterrupt:
      exit()
    except Exception as e:
      erro(f"erro: {e}")
