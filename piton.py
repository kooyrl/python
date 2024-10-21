# Realizar un programa que de solución a los siguientes problemas:

# Ingresar 5 alumnos (nombre,apellido y 3 notas)
# Nota 1 vale 20%
# Nota 2 vale 30% 
# Nota 3 vale 50%
# Calcular el promedio por alumno
# Calcular el promedio total del curso
# Calcular la mejor nota por alumno
# Calcular el mejor promedio


def promedio_curso(n1,n2,n3,n4,n5):
    prom = 0
    prom = (n1+n2+n3+n4+n5)/5
    return prom

def promedio_notas(n1,n2,n3,p1,p2,p3):
    prom = 0
    prom = (p1*n1+p2*n2+p3*n3)/100
    return prom

notas = [0,0,0]
alumnos = [0,0,0,0,0]

p = [20,30,50]
prom = [0,0,0,0,0]
print("Bienvenido a el Liceo Bicentenario Insuco")
print("")

for i in range(0,5,1):
    print(f"ALUMNO {i+1}")
    alumnos[i] = (input(f"Ingrese el nombre del alumno {i+1} :"))

    notas[0] = float(input("Ingrese la primera nota: "))
    notas[1] = float(input("Ingrese la segunda nota: "))
    notas[2] = float(input("Ingrese la tercera nota: "))

    prom[i] = promedio_notas(notas[0],notas[1],notas[2],p[0],p[1],p[2])
    print(f"El promedio del alumno {alumnos[i]} es {prom[i]}")

print(f"")