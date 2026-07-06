from ui.menus import menu_principal, menu_osint 
from ui.prompt import prompt_menu, prompt_osint, prompt_cpf
from modulos.osint.cpf import SisregConsulta  # Fixed import

def menu():
    while True:
        try:
            print(menu_principal)
            escolha = int(input(prompt_menu))  # Fixed variable name
            
            if escolha == 1:
                
                
            elif escolha == 2:
                print(menu_osint)
                escolha_osint = int(input(prompt_osint))  # Fixed variable name and added closing parenthesis
                
                if escolha_osint == 1:
                    print("Executando OSINT opção 1...")

                    
                elif escolha_osint == 2:
                    # Handle OSINT option 2
                    print("Executando OSINT opção 2...")
                    # Add your logic here
                    
                elif escolha_osint == 3:
                    cpf_input = input(prompt_cpf)  # Changed to string input for CPF
                    try:
                        cpf = int(cpf_input)  # Convert to int if needed
                        consulta = SisregConsulta(cpf)
                        print(f"Consulta realizada com sucesso para CPF: {cpf}")
                        # Process consulta result here
                    except ValueError:
                        print("CPF inválido. Digite apenas números.")
                        
                else:
                    print("Opção OSINT inválida!")
                    
            elif escolha == 3:
                # Handle exit or other option
                print("Saindo do sistema...")
                break
                
            else:
                print("Opção inválida! Tente novamente.")
                
        except ValueError:
            print("Erro: Digite apenas números!")
            continue
        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            continue

if __name__ == "__main__":
    menu()
