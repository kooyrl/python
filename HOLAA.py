# Función para calcular el promedio de un alumno
def calcular_promedio(notas):
    # Se asume que notas es una lista con 3 elementos [nota1, nota2, nota3]
    return notas[0] * 0.2 + notas[1] * 0.3 + notas[2] * 0.5

# Función para calcular el promedio total del curso
def promedio_curso(alumnos):
    suma = 0
    for alumno in alumnos:
        suma += calcular_promedio(alumno['notas'])
    return suma / len(alumnos)

# Función para encontrar la mejor nota de un alumno
def mejor_nota(alumno):
    return max(alumno['notas'])

# Función para encontrar el mejor promedio del curso y el alumno correspondiente
def mejor_promedio(alumnos):
    mejor = 0
    mejor_alumno = ""
    for alumno in alumnos:
        promedio = calcular_promedio(alumno['notas'])
        if promedio > mejor:
            mejor = promedio
            mejor_alumno = f"{alumno['nombre']} {alumno['apellido']}"
    return mejor, mejor_alumno

# Función para validar la entrada de una nota
def ingresar_nota(alumno, num_nota):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {num_nota} del alumno {alumno} (entre 1 y 7): "))
            if 1 <= nota <= 7:
                return nota
            else:
                print("Error: La nota debe estar entre 1 y 7.")
        except ValueError:
            print("Error: Por favor, ingrese la nota en números.")

# Función para validar el ingreso de nombre y apellido
def nombre_o_apellido(campo, num_alumno):
    while True:
        valor = input(f"Ingrese el {campo} del alumno {num_alumno}: ").strip()
        if valor:
            return valor
        else:
            print(f"Error: El {campo} no puede estar vacío.")

# Ingresar los datos de los 5 alumnos
alumnos = []
print("-----------------------")
print("")

for i in range(5):


    nombre = nombre_o_apellido("nombre", i + 1)
    apellido = nombre_o_apellido("apellido", i + 1)
    print("")
    notas = [ingresar_nota(nombre, j + 1) for j in range(3)]
    alumnos.append({'nombre': nombre, 'apellido': apellido, 'notas': notas})
    print("")
print("-----------------------")

# Mostrar resumen de cada alumno
for alumno in alumnos:
    print(f"\nResumen del alumno {alumno['nombre']} {alumno['apellido']}:")
    print(f"Notas: {alumno['notas']}")
    promedio = calcular_promedio(alumno['notas'])
    print(f"Promedio: {promedio:.2f}")

# Mostrar el promedio total del curso
print(f"\nEl promedio total del curso es: {promedio_curso(alumnos):.2f}")
print("")

# Mostrar la mejor nota de cada alumno
for alumno in alumnos:
    print(f"La mejor nota de {alumno['nombre']} {alumno['apellido']} es: {mejor_nota(alumno)}")

# Mostrar el mejor promedio del curso
mejor_prom, mejor_alumno = mejor_promedio(alumnos)
print(f"\nEl mejor promedio del curso es: {mejor_prom:.2f}, obtenido por: {mejor_alumno}")