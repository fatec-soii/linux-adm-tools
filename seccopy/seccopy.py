import os


def title():
    print("""
          
    ███████╗███████╗ ██████╗██╗   ██╗██████╗ ███████╗     ██████╗ ██████╗ ██████╗ ██╗   ██╗
    ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██╔════╝    ██╔════╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
    ███████╗█████╗  ██║     ██║   ██║██████╔╝█████╗      ██║     ██║   ██║██████╔╝ ╚████╔╝ 
    ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██╔══╝      ██║     ██║   ██║██╔═══╝   ╚██╔╝  
    ███████║███████╗╚██████╗╚██████╔╝██║  ██║███████╗    ╚██████╗╚██████╔╝██║        ██║   
    ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═════╝ ╚═╝        ╚═╝   

          """)


def menu():
    print("\nSelecione uma opção: \n")
    print("[ 1 ] - Fazer Cópia Segura")
    print("[ 2 ] - Criar chave RSA")
    print("[ 3 ] - Exportar chave RSA")
    print("[ 4 ] - Ativar servidor ssh")
    print("[ 5 ] - Desativar servidor ssh")
    print("[ 6 ] - Voltar para o menu principal")
    while True:
        try:
            opt = int(input(">>> "))
            if opt == 1:
                os.system("ls --color")
                arquivo = input("Informe o arquivo que deseja transferir:\n>>> ")
                usuario = input("Informe o nome de usuário da máquina remota:\n>>> ")
                ip = input("Informe o ip da máquina remota:\n>>> ")
                local = input("Informe o caminho que deseja salvar o arquivo:\n>>> ")
                os.system(f"scp {arquivo} {usuario}@{ip}:{local}")
            elif opt == 2:
                os.system("ssh-keygen -t rsa")
            elif opt == 3:
                usuario = input("Informe o nome de usuário da máquina remota:\n>>> ")
                ip = input("Informe o ip da máquina remota:\n>>> ")
                os.system(f"ssh-copy-id {usuario}@{ip}")
            elif opt == 4:
                os.system("systemctl start sshd")
                os.system("systemctl status sshd")
            elif opt == 5:
                os.system("systemctl stop sshd")
                os.system("systemctl status sshd")
            elif opt == 6:
                os.system("cls || clear")
                break
            else:
                print("Apenas as opções listadas estão disponíveis")
        except:
            print("Apenas as opções listadas estão disponíveis")
    
    
def main():
    os.system("cls || clear")
    title()
    menu()
    
if __name__ == "__main__":
    main()