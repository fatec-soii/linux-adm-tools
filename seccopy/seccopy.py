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
    while True:
        os.system("clear || cls")
        title()
        print("\nSelecione uma opção: \n")
        print("[ 1 ] - Fazer Cópia Segura")
        print("[ 2 ] - Fazer Login com o Secure Shell")
        print("[ 3 ] - Criar chave RSA")
        print("[ 4 ] - Exportar chave RSA")
        print("[ 5 ] - Ativar servidor ssh")
        print("[ 6 ] - Desativar servidor ssh")
        print("[ 7 ] - Voltar para o menu principal\n")
        try:
            opt = int(input(">>> "))
            if opt == 1:
                os.system("ls --color")
                arquivo = input("Informe o arquivo que deseja transferir:\n>>> ")
                usuario = input("Informe o nome de usuário da máquina remota:\n>>> ")
                ip = input("Informe o IP da máquina remota:\n>>> ")
                local = input("Informe o caminho que deseja salvar o arquivo:\n>>> ")
                os.system(f"scp {arquivo} {usuario}@{ip}:{local}")
                input("Aperte ENTER para continuar...")
            elif opt == 2:
                usuario = input("Informe o nome de usuário da máquina remota:\n>>> ")
                ip = input("Informe o número IP da máquina remota: \n>>> ")
                os.system(f"ssh {usuario}@{ip}")
            elif opt == 3:
                os.system("ssh-keygen -t rsa")
                input("Aperte ENTER para continuar...")
            elif opt == 4:
                usuario = input("Informe o nome de usuário da máquina remota:\n>>> ")
                ip = input("Informe o IP da máquina remota:\n>>> ")
                os.system(f"ssh-copy-id {usuario}@{ip}")
                input("Aperte ENTER para continuar...")
            elif opt == 5:
                os.system("sudo systemctl start sshd")
                input("Aperte ENTER para continuar...")
                os.system("sudo systemctl status sshd")
                input("Aperte ENTER para continuar...")
            elif opt == 6:
                os.system("sudo systemctl stop sshd")
                input("Aperte ENTER para continuar...")
                os.system("sudo systemctl status sshd")
                input("Aperte ENTER para continuar...")
            elif opt == 7:
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