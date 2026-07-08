from ui.menus import menu_osint
from ui.prompt import prompt_osint
from ui.mensagens import erro
from modulos.osint.ip import Ip
from core.carregar import carregar_json 

data = "config/ferramentas/osint.json"
ferramentas = carregar_json(data)

def painel_osint():
  while True:
    try:
      print(menu_osint)
      ot = int(input(prompt_osint))
      if str(ot) in ferramentas:
        ferramenta = ferramentas[str(ot)]
        
        if ferramenta["tipo"] == "str":
          parametro = input(ferramenta["parametro"])
          user = ferramenta["class"](*parametro)
          user.ferramenta["entrada"]()
          
        elif ferramenta["tipo"] == "int":
          parametro = int(input(ferramenta["parametro"]))
          user = ferramenta["class"](*parametro)
          user.ferramenta["entrada"]()
          
        elif ferramenta["tipo"] == "float":
          parametro = float(input(ferramenta["parametro"]))
          user = ferramenta["class"](*parametro)
          user.ferramenta["entrada"]()
      else:
        erro("somente numeros")
        continue
    except ValueError:
      erro("erro, somente numeros")
      continue
    except Exception as e:
      erro(f"erro: {e}")
