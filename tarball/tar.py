import os, tarfile, sys
from time import sleep


def list_tar():
    try:
        os.system("ls --color")
        file_path = input("\nInforme o arquivo que deseja listar: \n>>> ")
        with tarfile.open(file_path+'.tar.gz', 'r') as archive:
            archive.list()
            input("Pressione ENTER para continuar")
    except FileNotFoundError:
        print("[ERRO] Arquivo para listar não encontrado!")
    except tarfile.ReadError:
        print("[ERRO] Não é possivel ler o arquivo!")
    finally:
        print("Retornando ao menu...")
        sleep(2)
        main()
        
        
def extract_tar():
    try:
        file_path = input("Informe o arquivo que deseja extrair: \n>>> ")
        with tarfile.open(file_path+'.tar.gz', 'r') as archive:
            archive.extractall()
        print("Arquivos extraídos com sucesso!")
    except FileNotFoundError:
        print("[ERRO] Arquivo para extrair não encontrado!!!")
    finally:
        print("Retornando ao menu...")
        sleep(2)
        main()

def add_files_tar():
    try:
        file_path = input("Informe o nome do arquivo a ser criado: \n>>> ")
        extencao = input("Informe a extenção dos arquivos a serem adicionados: \n>>> ")
        with tarfile.open(file_path+'.tar.gz', 'w') as archive:
            for i in os.listdir():
                archive.add(i, filter = lambda x: x if x.name.endswith('.'+extencao) else None)
            print(f"Arquivos com a extensão {extencao} foram adicionados com sucesso.")
    except FileNotFoundError:
        print("[ERRO] Arquivos para adicionar não encontrados!!!")
    finally:
        print("Retornando ao menu...")
        sleep(2)
        main()


def menu():
    print("""
    ╔════╗        ╔╗       ╔╗ ╔╗ 
    ║╔╗╔╗║        ║║       ║║ ║║ 
    ╚╝║║╚╝╔══╗ ╔═╗║╚═╗╔══╗ ║║ ║║ 
      ║║  ╚ ╗║ ║╔╝║╔╗║╚ ╗║ ║║ ║║ 
     ╔╝╚╗ ║╚╝╚╗║║ ║╚╝║║╚╝╚╗║╚╗║╚╗
     ╚══╝ ╚═══╝╚╝ ╚══╝╚═══╝╚═╝╚═╝
     
     
     [ 1 ] Listar arquivos de um tarball
     [ 2 ] Extrair arquivos de um tarball
     [ 3 ] Criar um tarball e adicionar arquivos por extensão
     [ 4 ] Sair
    """)

def sair():
    os.system("cls || clear")
    pass


def selection():
    mode = True
    select = 0
    while mode:
        try:
            select = int(input(">>> "))
            if select > 0 or select < 5:
                mode = False
                break
        except:
            print("Somente números são permitidos.")
    return select


def switch_menu(opcao):
    opcoes = {
        1: list_tar,
        2: extract_tar,
        3: add_files_tar,
        4: sair
    }
    return opcoes.get(opcao, "Opção inválida.")


def main():
    os.system("cls || clear")
    menu()
    select = selection()
    switch = switch_menu(select)
    switch()
    
if __name__ == "__main__":
    main()
