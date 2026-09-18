from ui.menus.osint.cep import menu_bin
from ui.prompt.prompt_osint import prompt_bin
from ui.mensagens import erro, outro
from ui.color import azul
from modulos.osint.bin import Bin
from core.clear import clear
from config.ferramentas.ip import ferramentas_bin 
from config.APIS.api_bin import APIS_BIN
def painel_bin():
  while True:
    try:
      print(menu_bin)
      ot = int(input(prompt_bin))
      if ot == 0:
        clear()
        break
        
      if str(ot) in ferramentas_bin:
        api = ferramentas_bin[str(ot)]
        try:
          bin = int(input("bin > "))
        except ValueError:
          erro("somente numeros no cep")
          clear()
          continue 
        user = Bin(bin, api)
        user.BinBusca()
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
