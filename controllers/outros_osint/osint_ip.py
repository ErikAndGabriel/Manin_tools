from ui.menus import menu_ip
from ui.prompt import prompt_osint
from ui.mensagens import erro, outro
from modulos.osint.ip import Ip
from core.clear import clear
from config.ferramentas.ip import ferramentas_ip
from config.APIS.api_ip import APIS_IP 
def painel_ip():
  while True:
    try:
      print(menu_ip)
      ot = int(input(prompt_osint))
      if ot == 0:
        clear()
        break
        
      if str(ot) in ferramentas_ip:
        nome = ferramentas_ip[str(ot))
        api = APIS_IP[nome]["url"]
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
