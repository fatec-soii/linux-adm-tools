import os
from time import sleep


def menu():
    print("""
                            Gerenciador de 
        ░▄▀▀▄░█▀▀▄░▄▀▀▄░▄▀▀▄░█▀▀▄░░▀░░█▀▀░▀█▀░█▀▀▄░█▀▀▄░░▀░░▄▀▀▄
        ░█▄▄█░█▄▄▀░█░░█░█▄▄█░█▄▄▀░░█▀░█▀▀░░█░░█▄▄█░█▄▄▀░░█▀░█░░█
        ░█░░░░▀░▀▀░░▀▀░░█░░░░▀░▀▀░▀▀▀░▀▀▀░░▀░░▀░░▀░▀░▀▀░▀▀▀░░▀▀░
    
    """)
    os.system("ls -l --color")
    print()


def file_path():
    file = input("\nInforme o caminho do arquivo/diretorio que deseja alterar a propriedade: \n>>> ")
    if not os.path.exists(file):
        print("O arquivo/diretorio não existe!")
        return main()
    print("Arquivo encontrado!")
    return file


def make_owner(file):
    try:
        name = input("Infome o nome do novo proprietário:\n>>> ")
        group = input("Informe a que grupo o arquivo pertence:\n>>> ")
        os.system(f"chown -R -c {name}:{group} {file}")
        sleep(3)
        os.system("clear || cls")
    except:
        print("Nome de Usuário ou Grupo inexistente.")
        print("Retornando ao menu inicial...")
        sleep(2)
        main()


def main():
    os.system("cls || clear")
    menu()
    file = file_path()
    if file:
        make_owner(file)
        


if __name__ == "__main__":
    main()
