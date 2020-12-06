import subprocess 
import os
import sys 
import getpass 


def banner():
    os.system("clear || cls")
    print("""
                     Gerenciamento de 
██╗   ██╗███████╗██╗   ██╗ █████╗ ██████╗ ██╗ ██████╗ ███████╗
██║   ██║██╔════╝██║   ██║██╔══██╗██╔══██╗██║██╔═══██╗██╔════╝
██║   ██║███████╗██║   ██║███████║██████╔╝██║██║   ██║███████╗
██║   ██║╚════██║██║   ██║██╔══██║██╔══██╗██║██║   ██║╚════██║
╚██████╔╝███████║╚██████╔╝██║  ██║██║  ██║██║╚██████╔╝███████║
 ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚══════╝

    [ 1 ] Adicionar usuário
    [ 2 ] Deletar usuário
    [ 3 ] Voltar ao menu principal
    
          """)
    

def add_user():
     username = input("Informe o nome de usuário a ser criado:\n>>> ")    
     password = getpass.getpass()
     try: 
         subprocess.run(['useradd', '-p', password, username ])       
     except: 
         print(f"Falha ao criar o usuário.")                      
         sys.exit(1) 


def del_user(): 
     username = input("Informe o nome do usuário a ser deletado:\n>>> ") 
     try: 
         output = subprocess.run(['userdel', username ]) 
         if output.returncode == 0: 
             print("Usuário deletado com sucesso!") 
     except:
         print(f"Falha ao deletar o usuário.") 
         sys.exit(1) 


def selection():
    mode = True
    select = 0
    while mode:
        try:
            select = int(input(">>> "))
            if select == 1 or select == 2 or select == 3:
                mode = False
                break
        except:
            print("Somente números são permitidos.")
    return select


def switch_menu(opcao):
    opcoes = {
        1: add_user,
        2: del_user,
        3: voltar,
    }
    return opcoes.get(opcao, "Opção inválida.")


def voltar():
    os.system("clear || cls")
    pass


def main():
    banner()
    select = selection()
    switch = switch_menu(select)
    switch()

if __name__ == "__main__":
    main()
