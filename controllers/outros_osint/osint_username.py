from ui.prompt.prompt_osint import prompt_user_name
from ui.menus.osint.user_name import menu_user_name
from ui.mensagens import outro, sucesso, erro
from modulos.osint.user_name import UserName
def painel_user_name():
    while True:
        try:
           print(menu_user_name)
           escolha = int(input(prompt_user_name))
           if escolha == 1:
              user = input(f"user_name {prompt_user_name})
              usuario = UserName(user)
              usuario.buscar()
              outro()
           elif escolha == 0:
              break
           else:
              erro("escolha invalida")
              continue
        except ValuerError:
            erro("somente numeros")
            continue
        except Exception as e:
            erro(f"error: {e}")
            continue
