#Oscar Daniel Alejandro Lopez Ramirez
#NUMERO

import pyfiglet
from colorama import init, Fore, Back, Style

init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

n = int(input("introduce in numero entero positivo:"))
for i in range(1, n+1, 2):
    print(i, end=", ")