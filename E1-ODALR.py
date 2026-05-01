#Oscar Daniel Alejandro Lopez Ramirez
#Registro de asistencia

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

print("---- Programa asistencia ----")
#Se ingresan la cantidad de empleados registrados
empleados_actuales = int(input("Ingrese la cantidada de empleados que hay actualmente: "))
#conteo que se usara para delimitar la lista de empleados
conteo = 0
#almacen para los nombre de los empleados
asistentes = []
#bucle que permitira que el ingreso de los empleados al almacen
while conteo < empleados_actuales:
    #Se usa para para agregar el nombre uno por uno
    nombre_empleado = input(f"Ingrese el nombre del empleado NO.{conteo + 1}: ")
    #ingreso de los nombres
    asistentes.append(nombre_empleado)
    #mensaje de notificacion tras un ingreso exitoso
    print(f"{conteo} ha sido registrado.")
    #suma uno al contador para que iguale a los empleados
    conteo += 1
#mensaje tras completar la lista de empleados
print("Listado completo: ")
for persona in asistentes:
    print("- " + persona)