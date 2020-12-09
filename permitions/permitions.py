import os
from time import sleep

def banner():
    print("""
                        Gerenciador de
        ░▄▀▀▄░█▀▀░█▀▀▄░█▀▄▀█░░▀░░█▀▀░█▀▀░▄▀▀▄░█▀▀░█▀▀
        ░█▄▄█░█▀▀░█▄▄▀░█░▀░█░░█▀░▀▀▄░▀▀▄░█░░█░█▀▀░▀▀▄
        ░█░░░░▀▀▀░▀░▀▀░▀░░▒▀░▀▀▀░▀▀▀░▀▀▀░░▀▀░░▀▀▀░▀▀▀
    
    """)
    os.system("ls -l --color")
    print()


def choose():
    print("Menu - Alterar a propriedade:\n")
    print("[ 1 ] - Diretório")
    print("[ 2 ] - Arquivo")
    print("[ 3 ] - Listar diretório atual")
    print("[ 4 ] - Retornar para o menu principal\n")
    option = 0
    while True:
        try:
            option = int(input(">>> "))
            if option == 1:
                break
            if option == 2:
                break
            if option == 3:
                break
            if option == 4:
                break
            else:
                print("Apenas as opções informadas são disponíveis!")
        except:
            print("Apenas as opções informadas são disponíveis!")
    return option


def dir_path():
    print()
    dir = input("\nInforme o diretório que deseja alterar a propriedade: ")
    if not os.path.exists(dir):
        print("O diretório não existe!")
        sleep(2)
        return main()
    print("Diretório encontrado!")
    return dir


def file_path():
    print()
    file = input("\nInforme o arquivo que deseja alterar a propriedade: ")
    if not os.path.exists(file):
        print("O arquivo não existe!")
        sleep(2)
        return main()
    print("Arquivo encontrado!")
    return file


def define_property():
    name_list = ["USUÁRIO", "GRUPO", "OUTROS"]
    cont = 0
    comando = ''
    while cont < 3:
        print(f"""
        Para {name_list[cont]} qual permissão será concedida?

        0 - permissao negada
        1 - execucao
        2 - escrita
        4 - leitura
        5 - execucao e leitura
        6 - escrita e leitura
        7 - permissao total\n""")
        try:
            opcao = int(input("Insira apenas um ÚNICO número \n>>> "))
            if opcao >= 0 and opcao <= 7 and opcao != 3:
                comando += str(opcao)
                cont += 1
        except:
            print("Somente os números disponíveis no menu são permitidos.")
    return comando


def exec_property(command, file, opt):
    if opt == 1:
        try:
            os.system(f'chmod -cvR {command} {file}')
            print()
            os.system("ls -l --color")
        except:
            print("Ocorreu um erro, tente novamente!")
    if opt == 2:
        try:
            os.system(f'chmod -cv {command} {file}')
            print()
            os.system("ls -l --color")
        except:
            print("Ocorreu um erro, tente novamente!")


def main():
    os.system("cls || clear")
    banner()
    option = choose()
    try:
        if option == 1:
            dir = dir_path()
            command = define_property()
            exec_property(command, dir, 1)
            sleep(2)
            choose()
        if option == 2:
            file = file_path()
            command = define_property()
            exec_property(command, file, 2)
            sleep(2)
            choose()
        if option == 3:
            os.system("ls -l --color")
            sleep(2)
            choose()
        if option == 4:
            sleep(1)
            os.system("cls || clear")
            pass #retornar menu inicial
            
    except:
        print("Algo deu errado, tente novamente!")


if __name__ == "__main__":
    main()