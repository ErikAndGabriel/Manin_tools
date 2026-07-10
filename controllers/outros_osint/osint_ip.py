from ui.menu import menu_ip
from ui.prompt import prompt_osint
from ui.mensagens import erro, outro
from modulos.osint.ip import Ip
from core.clear import clear
from config.ferramentas.osint import ferramentas_ip

def painel_ip():
  while True:
    try:
      print(menu_ip)
      ot = int(input(prompt_ip))
      if ot == 0:
        clear()
        break
        
      if str(ot) in ferramentas_ip:
        api = ferramentas_ip[str(ot)]
        prompt = input("ip > ")
        user = Ip(prompt, api)
        user.IpBusca()
        outro()
        continue
        
      else:
        erro("escolha invalida")
        continue
    except ValueError:
      erro("somente numeros")
      continue
    except Exception as e:
      erro(f"erro: {e}")
