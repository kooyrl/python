def promedio(a,b,c):
    prom= (a + b + c)/3
    return prom 


print("Bienvenido a la calculadora pitona")
print("")

contfem = 0
contmas = 0
hom_notas = 0

ca = int(input("Ingrese cantidad de alumnos: "))
print("")
for i in range(0,ca,1):
    nom = input("Ingrese el nombre del alumno: ")
    print("")
    print("")
    print("Ingrese notas")
    nota1 = float(input("NOTA 1: "))
    nota2 = float(input("NOTA 2: "))
    nota3 = float(input("NOTA 3: "))
    pro=promedio(nota1,nota2,nota3)
    print("")
    genero = input("Ingrese el genero del alumno M/F: ")
    print("")
    if(genero=="F"):
        contfem = contfem + 1
        print("+ 1 Femenino")
        print("")
    else:
        contmas = contmas + 1
        print("+ 1 Masculino")
        hom_notas = hom_notas + nota1 + nota2 + nota3
        print("")
    print("El promedio del alumno es ",pro)

prom_hom = hom_notas / contmas

print("El promedio de notas de todos los hombres es: ",prom_hom)
print("")