import os
from time import sleep

def banner():
    print("""
    ░░░░░░   ░░░░░   ░░░░░░ ░░   ░░ ░░    ░░ ░░░░░░      ░░░░░░  ░░    ░░ 
    ▒▒   ▒▒ ▒▒   ▒▒ ▒▒      ▒▒  ▒▒  ▒▒    ▒▒ ▒▒   ▒▒     ▒▒   ▒▒  ▒▒  ▒▒  
    ▒▒▒▒▒▒  ▒▒▒▒▒▒▒ ▒▒      ▒▒▒▒▒   ▒▒    ▒▒ ▒▒▒▒▒▒      ▒▒▒▒▒▒    ▒▒▒▒   
    ▓▓   ▓▓ ▓▓   ▓▓ ▓▓      ▓▓  ▓▓  ▓▓    ▓▓ ▓▓          ▓▓         ▓▓    
    ██████  ██   ██  ██████ ██   ██  ██████  ██          ██         ██    

          """)


def get_source():
    source = str(input("Entre com o caminho de origem: "))

    while(os.path.isdir(source) == False):
        source = str(
            input(f"{source} este não é um caminho válido!\nEntre com o caminho de origem:"))
    return source


def get_destination():
    destination = str(input("Entre com o caminho de destino: "))

    while(os.path.isdir(destination) == False):
        destination = str(
            input(f"{destination} este não é um caminho válido!\nEntre com o caminho de destino:"))
    return destination


def backup(source, destination):
    os.system(f'rsync -avc {source} {destination}')
    input("Aperte ENTER para continuar...")
    os.system("clear || cls")


def execute():
    source = get_source()
    destination = get_destination()
    backup(source, destination)
    sleep(2)
    os.system("clear || cls")


def main():
    os.system("cls || clear")
    banner()
    execute()