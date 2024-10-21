# Crear un programa en python que:
# Ingrese trabajadores mientras el sueldo sea distinto de CERO
# Ingresar nombre y sueldo
# Ordenar del mejor sueldo al más bajo

import os

def limpiar_pantalla():
    os.system('cls')

limpiar_pantalla()
def validar_sueldo():
    sueldo = 0
    while ((sueldo < 500000) or (sueldo > 5000000)):
        sueldo = float(input("Ingrese el sueldo del trabajador (0 para terminar): "))
        try:
            if (sueldo < 500000 and sueldo!=0):
                print("Sueldo no válido, tiene que estar entre $500.000 - $5.000.000")
                print("")
                a = input("Presione ENTER para continuar...")
                limpiar_pantalla()
            if (sueldo > 5000000):
                print("Sueldo no válido, tiene que estar entre $500.000 - $5.000.000")
                print("")
                a = input("Presione ENTER para continuar...")
                limpiar_pantalla()
            if (sueldo == 0):
                print("Chau")
                break
            if (sueldo != 0 and sueldo > 500000 and sueldo < 5000000):
                print("*** Sueldo bien ingresado ***")
                print("")
                a = input("Presione ENTER para continuar...")
                limpiar_pantalla()
        except ValueError:
            print("Por favor, ingrese un número válido, no letras ni otro tipo de carácter.")
            print("")
            a = input("Presione ENTER para continuar...")
            limpiar_pantalla()
            continue
    return sueldo
nombres = []
sueldos = []
cont = 0

print("Bienvenido")
print("")

sueldo = validar_sueldo()
while (sueldo != 0):
    cont += 1
    nombre = input(f"Ingrese nombre del trabajador {cont}...")
    limpiar_pantalla()
    sueldo = validar_sueldo()
    nombres.append(nombre)
    sueldos.append(sueldo)

for i in range(cont):
    for j in range(0,cont - 1 - i):
        if sueldos[j] < sueldos[j + 1]:
            sueldos[j],sueldos[j+1] = sueldos[j+1],sueldos[j]
            nombres[j],nombres[j+1]=nombres[j+1],nombres[j]

for k in range(len(sueldos)):
    print("--------------------------------")
    print(f"Nombre {k+1}: {nombres[k]}")
    print(f"Sueldo {k+1}: {sueldos[k]}")
    print("--------------------------------")
    print("")
    a = input("Presione ENTER para continuar...")
    limpiar_pantalla()