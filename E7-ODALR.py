#Oscar Daniel Alejandro Lopez Ramirez
#El pastel es una mentira

import pyfiglet
from colorama import init, Fore, Back, Style

init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)
#Usario ingresa su clave y el programa la guarda
clave = int(input("Ingrese su clave: "))
#El bucle imprimirá el mensaje una cantidad equivalente a su clave
for i in range(clave):
    print("Usted es clave: " + str(i + 1))
