####### Drag "yuna.py" to your folder.
from yuna import yuna
####### git clone https://github.com/yuriwithdaggers/yuna.git

from colorama import Fore, Back, Style, init
init(convert=True)
import json


def nicks():
    try:
        with open('nicks.txt', 'r') as f:
            f = f.read().replace("\n", " ")
        return f
    except (AttributeError, FileNotFoundError):
        print('Make sure there is a nicks.txt in the folder')

def check():
    try:
        kek = nicks()
        i = kek.strip(' ').split(' ')
        for nick in i:
            r = yuna('get', f'/lol-summoner/v1/check-name-availability/{nick}')
            r = json.loads(r.content)
            if r == False:
                print(Fore.BLACK + Back.RED + f"[ x ] Nick '{nick}' -> Unavailable" + Style.RESET_ALL)
            elif r == True:
                print(Fore.BLACK + Back.GREEN + f"[ ! ] Nick '{nick}' -> Available" + Style.RESET_ALL)
        print(Fore.BLACK + Back.WHITE + f"[ & ] Done. Press any key to exit." + Style.RESET_ALL)

    except:
        print("Make sure your lol is open.")




def main():
    print(Fore.RED + """
        ███▄    █  ██▓ ▄████▄   ██ ▄█▀                   
        ██ ▀█   █ ▓██▒▒██▀ ▀█   ██▄█▒                    
        ▓██  ▀█ ██▒▒██▒▒▓█    ▄ ▓███▄░                    
        ▓██▒  ▐▌██▒░██░▒▓▓▄ ▄██▒▓██ █▄                    
        ▒██░   ▓██░░██░▒ ▓███▀ ░▒██▒ █▄                   
        ░ ▒░   ▒ ▒ ░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒                   
        ░ ░░   ░ ▒░ ▒ ░  ░  ▒   ░ ░▒ ▒░                   
            ░   ░ ░  ▒ ░░        ░ ░░ ░                    
                ░  ░  ░ ░      ░  ░                      
                        ░                                  
    ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
    ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
    ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
    ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
    ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
    ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
    ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
    ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
    ░                       ░                               

    """ + Style.RESET_ALL)
    check()
    input()

if __name__ == "__main__":
    main()