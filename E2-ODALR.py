#Oscar Daniel Alejandro Lopez Ramirez
#lista de tareas pendientes

import pyfiglet
from colorama import init, Fore, Back, Style

init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

print("---- Programa Tareas Pendientes ----")
#ingresa la cantidad de treas a guardar
tareas_cantidad = int(input("Ingrese sus tareas pendientes: "))
#Se encarga de guardar las tareas dentro de la matriz
tareas = []
#bucle inicial encargado de guardar las tareas
for i in range(tareas_cantidad):
    #Ingresa y guarda el nombre de la tarea
    tarea = input(f"ingrese la tarea que desea guardar NO.{i + 1}: ")
    #agrega la tarea escrita a la lista
    tareas.append(tarea)
#mensaje de guardado exitoso
print("Tareas registradas:")
#imprime las tareas guardadas y el numero en que fue guardada
for i in range(len(tareas)):
    print(f"Tarea {i + 1}: {tareas[i]}")
