#Oscar Daniel Alejandro Lopéz Ramirez
#Carga de servidores

import pyfiglet
from colorama import init, Fore, Back, Style

init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

print("---- Simulador de carga de servidores ----")
#Guarda la cantidad de servidores que se desean usar para las cargas
servidor = int(input("Cual es la cantidad de servidores a cargar?: "))
#Guarda el numero de procesos que se van a hacer por cada servidor
procesos = int(input("Cuantos procesos por servidor?: "))
#bucle que sumara y creara un servidor hasta igualar la cantidad de servidores ingresados
for i in range(1, servidor + 1):
    #Mensaje de cada servidor creado
    print(f"Servidor NO.{i}: ")
    #bucle que creara un mensaje de proceso hasta igualar la cantidad ingresada
    for j in range(1, procesos + 1):
        #Mensaje que se creara tras generar cada proceso por servidor
        print(f" Cargando procesos {j}...")
        