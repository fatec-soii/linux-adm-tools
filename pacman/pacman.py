import os


def title():
    os.system("cls || clear")
    print("""
                 Gerenciador de 
          
██████╗  █████╗  ██████╗ ██████╗ ████████╗███████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔═══██╗╚══██╔══╝██╔════╝██╔════╝
██████╔╝███████║██║     ██║   ██║   ██║   █████╗  ███████╗
██╔═══╝ ██╔══██║██║     ██║   ██║   ██║   ██╔══╝  ╚════██║
██║     ██║  ██║╚██████╗╚██████╔╝   ██║   ███████╗███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝


          """)


def pacman():
    while True:
        print("\nSelecione uma opção: \n")
        print("[ 1 ] - Instalar pacotes")
        print("[ 2 ] - Listar pacotes instalados")
        print("[ 3 ] - Atualizar pacotes")
        print("[ 4 ] - Desinstalar pacotes")
        print("[ 5 ] - Consultar dependências de pacotes")
        print("[ 6 ] - Procurar por pacotes")
        print("[ 7 ] - Instalar pacotes essenciais")
        print("[ 8 ] - Voltar para o menu principal")
        try:
            opt = int(input("\n >>> "))
            if opt == 1:
                pacote = input("Instalar >>> ")
                os.system(f"pacman -S {pacote}")
            elif opt == 2:
                os.system(f"pacman -Q")
            elif opt == 3:
                pacote = input("Atualizar >>> ")
                os.system(f"pacman -Syuu {pacote}")
            elif opt == 4:
                pacote = input("Desinstalar >>> ")
                os.system(f"pacman -R {pacote}")
            elif opt == 5:
                pacote = input("Procurar Dependencias >>> ")
                os.system(f"pacman -Q {pacote}")
            elif opt == 6:
                pacote = input("Procurar Pacotes >>> ")
                os.system(f"pacman -Ss {pacote}")
            elif opt == 7:
                os.system("pacman -S apache php-apache links cronie man base-devel bc distcc git pkgfile rsync openssh unzip")
            elif opt == 8:
                os.system("cls || clear")
                break
            else:
                print("Apenas as opções listadas estão disponíveis")
        except:
            print("Apenas as opções listadas estão disponíveis")
    

   
def main():
    title()
    pacman()


if __name__ == "__main__":
    main()
