from ui.menus.osint.telegram import menu_telegram, menu_bot, menu_token_conta
from ui.prompt import prompt_telegram, prompt_telegram_bot, prompt_telegram_conta
from ui.mensagens import erro, outro
from core.clear import clear
from modulos.osint.telegram_info_bot import BotTelegramInfo
from modulos.osint.telegram_info_chat import ChatTelegramInfo

def painel_telegram():
    while True:
        try:
            clear()
            print(menu_telegram)
            escolha = int(input(prompt_telegram))
            if escolha == 1:
                while True:
                    try:
                        clear()
                        print(menu_bot)
                        escolha_bot = int(input(prompt_telegram_bot))
                        if escolha_bot == 1:
                            chat_id = input(f"chat id {prompt_telegram}")
                            bot_token = input(f"bot token {prompt_telegram}")
                            user = ChatTelegramInfo(
                                bot_token,
                                chat_id
                            )
                            user.Buscar()
                            outro()
                        elif escolha_bot == 2:
                            bot_token = input(f"bot token {prompt_telegram}")
                            user = BotTelegramInfo(
                                bot_token
                            )
                            user.Buscar()
                            outro()
                        elif escolha_bot == 0:
                            clear()
                            break
                        else:
                            erro("escolha invalida")
                            outro()
                    except ValueError:
                        erro("somente numeros")
                        outro()
                    except KeyboardInterrupt:
                        clear()
                        break
                    except Exception as e:
                        erro(f"erro: {e}")
                        outro()
            elif escolha == 2:
                while True:
                    try:
                        clear()
                        print(menu_token_conta)
                        escolha_conta = int(
                            input(prompt_telegram_conta)
                        )
                        if escolha_conta == 0:
                            clear()
                            break
                        else:
                            erro("opção ainda não implementada")
                            outro()
                    except ValueError:
                        erro("somente numeros")
                        outro()
                    except KeyboardInterrupt:
                        clear()
                        break
                    except Exception as e:
                        erro(f"erro: {e}")
                        outro()
            elif escolha == 0:
                clear()
                break
            else:
                erro("escolha invalida")
                outro()
        except ValueError:
            erro("somente numeros")
            outro()
        except KeyboardInterrupt:
            clear()
            break
        except Exception as e:
            erro(f"erro: {e}")
            outro()
