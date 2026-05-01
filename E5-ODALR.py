#Oscar Daniel Alejandro Lopez Ramirez
#Registros de apartamentos

import pyfiglet
from colorama import init, Fore, Back, Style

init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

print("---- Registros de apartamentos ----")
#Input Guarda la cantidad de departamento que estan disponibles en el momento
departamentos = int(input("Ingrese la cantidad de departamentos disponibles: "))
#Genera una matriz para poder guardar el nombre de los departamentos
departamentos_nombre = []
#Se crea un bucle que guardara y designara un numero a cada departamento
#En base a la cantidad ingresada anteriormente
for i in range(departamentos):
    #Le asignara un nombre numero al departamento de turno
    nombre = input(f"Nombre del departamento NO.{i + 1}: ")
    #Guardara el numero dentro de la matriz
    departamentos_nombre.append(nombre)
    #El usuario le asignara el nombre a cada departamento y se guardara en la matriz
    puestos = int(input(f"Cuales con los puestos del deparamento {nombre}?: "))
    #El usuario le dara un puesto a cada departamento
    print(f"Puestos en el departamento {nombre}: ")

    