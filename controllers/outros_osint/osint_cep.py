from ui.menus import menu_cep
from ui.prompt import prompt_osint
from ui.mensagens import erro, outro
from ui.color import azul
from modulos.osint.cep import Cep
from core.clear import clear
from config.ferramentas.ip import ferramentas_cep
from config.APIS.api_cep import APIS_CEP
def painel_cep():
  while True:
    try:
      print(menu_cep)
      ot = int(input(prompt_osint))
      if ot == 0:
        clear()
        break
        
      if str(ot) in ferramentas_cep:
        api = ferramentas_cep[str(ot)]
        try:
          cep = int(input("cep > "))
        except ValueError:
          erro("somente numeros no cep")
          clear()
          continue 
        user = Cep(cep, api)
        user.CepBusca()
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
