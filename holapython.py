# Esto es un comentario
from os import system
system("cls")
print("")
print("Hola.... Bienvenido a la Calculadora Institutana")
print("")

num1 = 0
num2 = 0
num3 = 0

def suma (a,b):
    return a + b

def resta (a,b):
    return a - b

def division (a,b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def multiplicacion (a,b):
    return a * b

def promedio (a,b,c):
    return (a+b+c) / 3

def mostrar_menu():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

def calculadora():
    while True:
        mostrar_menu()
        seleccion = input("Introduce el número de la operación deseada (1/2/3/4) o 'q' para salir: ")

        if seleccion == 'q':
            print("Saliendo de la calculadora...")
            break

        if seleccion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
            except ValueError:
                print("Error: Introduce un número válido.")
                continue

            if seleccion == '1':
                print("Resultado:", suma(num1, num2))
            elif seleccion == '2':
                print("Resultado:", resta(num1, num2))
            elif seleccion == '3':
                print("Resultado:", multiplicacion(num1, num2))
            elif seleccion == '4':
                print("Resultado:", division(num1, num2))
        else:
            print("Selección inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    calculadora()








print("*** RESPUESTAS ***")
print("")
print("El resultado de la suma de ambos números es: ", suma(num1,num2))
print("El resultado de la resta de ambos números es: ", resta (num1,num2))
print("El resultado de la división de ambos números es: ", division (num1,num2))
print("El resultado de la multiplicación de ambos números es: ", multiplicacion (num1,num2))
print("El promedio de los tres números ingresados es: ", promedio (num1,num2,num3))