#Oscar Daniel Alejandro Lopez Ramirez
#Crear una palabra y imprimirla luego

import pyfiglet
from colorama import init, Fore, Back, Style

init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

#El usuario ingresa una palabra
word = input("Ingrese una palabra: ")
#El bucle imprimira la palabra 10 veces
for i in range(10):
    print(word)

    