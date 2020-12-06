import os
import sys
from time import sleep
from tarball.tar import main as maintar
from owner.owner import main as mainown
from seccopy.seccopy import main as mainsec
from permitions.permitions import main as mainper
from backuppy.backup import main as mainback
from add_user.add_user import main as mainadd
from pacman.pacman import main as mainpac


def is_root():
    euid = os.geteuid() 
    if euid != 0:
        print("É necessário acesso ROOT para executar este programa.")
        sleep(1.5)
        print("Saindo...")
        sys.exit()


def banner_menu():
    print("""

      ______   ______                   ______ ______ 
     /      \ /      \                 |      \      \\
    |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\                 \▓▓▓▓▓▓\▓▓▓▓▓▓
    | ▓▓___\▓▓ ▓▓  | ▓▓     ______       | ▓▓   | ▓▓  
     \▓▓    \| ▓▓  | ▓▓    |      \      | ▓▓   | ▓▓  
     _\▓▓▓▓▓▓\ ▓▓  | ▓▓     \▓▓▓▓▓▓      | ▓▓   | ▓▓  
    |  \__| ▓▓ ▓▓__/ ▓▓                 _| ▓▓_ _| ▓▓_ 
     \▓▓    ▓▓\▓▓    ▓▓                |   ▓▓ \   ▓▓ \\
      \▓▓▓▓▓▓  \▓▓▓▓▓▓                  \▓▓▓▓▓▓\▓▓▓▓▓▓


    Tema: Criação de Ferramentas de Administração Linux
    """)

    print("""
    Menu:

    [ 1 ] - Copia Segura
    [ 2 ] - Gerenciador Tarball
    [ 3 ] - Gerenciador de Permissoes
    [ 4 ] - Gerenciamento de Usuários
    [ 5 ] - Mudança de Proprietário
    [ 6 ] - Backup System
    [ 7 ] - Gerenciador de Pacotes
    [ 8 ] - Sair
    """)

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
        1: mainsec,
        2: maintar,
        3: mainper,
        4: mainadd,
        5: mainown,
        6: mainback,
        7: mainpac,
        8: sair
    }
    return opcoes.get(opcao, "Opção inválida.")


def sair():
    os.system("cls || clear")
    sys.exit()


def main():
    os.system("cls || clear")
    is_root()
    while True:
        banner_menu()
        select = selection()
        switch = switch_menu(select)
        switch()


if __name__ == "__main__":
    main()
