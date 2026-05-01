#Oscar Daniel Alejandro Lopez Ramirez
#Similador de logs

import pyfiglet
from colorama import init, Fore, Back, Style

init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

print("---- Simulador de logs de errores ----")
#Guarda la cantidad ingresada en la variable
error = int(input("Cuantos logs de errores desea crear?: "))
#Utiliza la Cantidad guardada y crea un bucle que suma 1 hasta que sea igual
#A la cantidad ingresada
for i in range(1, error + 1):
    #Crea los errores simulados y agrega el numero del rango a el conteo
    #De errores, imprimiéndolo junto a el mensaje
    print(f"ERROR NO.{i} Fallo detectado en la base de datos")