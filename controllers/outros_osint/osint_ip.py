from ui.menus import menu_ip
from ui.prompt import prompt_ip
from ui.mensagens import erro, outro
from modulos.osint.ip import Ip
from core.clear import clear
from config.ferramentas.ip import ferramentas_ip
from config.APIS.api_ip import APIS_IP 
def painel_ip():
  while True:
    try:
      print(menu_ip)
      ot = int(input(prompt_ip))
      if ot == 0:
        clear()
        break
        
      if str(ot) in ferramentas_ip:
        nome = ferramentas_ip[str(ot)]
        prompt = input(f"ip {prompt_ip}")
        user = Ip(prompt, nome)
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
