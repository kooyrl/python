# Crear un programa en Python para INSUCO STREAMING

# - Ingresar N películas
# - Cada película tiene:
#       * Nombre de la película
#       * Protagonista
#       * Antagonista
#       * Director
#       * Género
#       * Año de estreno
#       * Cantidad de visualizaciones o vistas

# - Crear una función para validar GÉNERO
#       (Acción, Terror, Comedia, Romance e Infantil)
# - Crear otra función para validar AÑO (2000-2024)
# - Mostrar película más vista
# - Mostrar película menos vista
# - Calcular promedio de visualizaciones o vistas
# - Sumar cantidad de películas de acción y almacenarlas en un nuevo ARRAY

# Se debe implementar ARRAY o ARREGLO

def limp_pantalla():
    from os import system
    system("cls")
    return limp_pantalla

def validar_genero(genero):
    generos_validos = ['Acción', 'Terror', 'Comedia', 'Romance', 'Infantil']
    return genero in generos_validos

def validar_año(año):
    return 2000 <= año <= 2024

def main():
    peliculas = []

    limp_pantalla()

    print("*** Bienvenido a Insuco Streaming ***")
    print("")
    N = int(input("Ingrese la cantidad de películas que quiere ingresar..."))
    limp_pantalla()
    print(f">>> SE INGRESARÁN {N} PELÍCULAS <<<")
    print("")
    a = input("Presione ENTER para continuar...")

    for i in range(N):
        limp_pantalla()
        print(f"** Película {i + 1} **")
        print("")
        nombre = input(f"Ingrese el nombre de la película {i + 1}...")
        limp_pantalla()
        protagonista = input(f"Ingrese el nombre del protagonista de {nombre}: ")
        limp_pantalla()
        antagonista = input(f"Ingrese el nombre del antagonista de {nombre}: ")
        limp_pantalla()
        director = input(f"Ingrese el nombre del director de {nombre}: ")
        limp_pantalla()

        while True:
            genero = input("Género (Acción, Terror, Comedia, Romance, Infantil): ")
            if validar_genero(genero):
                break
            else:
                limp_pantalla()
                print("Género inválido. Inténtelo de nuevo.")

        while True:
            limp_pantalla()
            año = int(input("Año de estreno (2000-2024): "))
            if validar_año(año):
                break
            else:
                print("Año inválido. Inténtelo de nuevo.")
        limp_pantalla()
        vistas = int(input("Cantidad de visualizaciones: "))
        print("")
        peliculas.append({
            'nombre': nombre,
            'protagonista': protagonista,
            'antagonista': antagonista,
            'director': director,
            'genero': genero,
            'año': año,
            'vistas': vistas
        })
        a = input("Presione ENTER para continuar...")

    if not peliculas:
        print("No se han ingresado películas.")
        return

    max_vistas = -1
    min_vistas = float('inf')
    total_vistas = 0
    contador_accion = 0

    for pelicula in peliculas:
        if pelicula['vistas'] > max_vistas:
            max_vistas = pelicula['vistas']
            pelicula_mas_vista = pelicula

        if pelicula['vistas'] < min_vistas:
            min_vistas = pelicula['vistas']
            pelicula_menos_vista = pelicula

        total_vistas += pelicula['vistas']

        if pelicula['genero'] == 'Acción':
            contador_accion += 1

    promedio_vistas = total_vistas / len(peliculas)

    print("\n*** Película más vista ***")
    print("")
    print(f"Nombre: {pelicula_mas_vista['nombre']}")
    print(f"Protagonista: {pelicula_mas_vista['protagonista']}")
    print(f"Antagonista: {pelicula_mas_vista['antagonista']}")
    print(f"Director: {pelicula_mas_vista['director']}")
    print(f"Género: {pelicula_mas_vista['genero']}")
    print(f"Año: {pelicula_mas_vista['año']}")
    print(f"Visualizaciones: {pelicula_mas_vista['vistas']}")
    print("")
    a = input("Presione ENTER para continuar...")
    limp_pantalla()

    print("\n*** Película menos vista ***")
    print("")
    print(f"Nombre: {pelicula_menos_vista['nombre']}")
    print(f"Protagonista: {pelicula_menos_vista['protagonista']}")
    print(f"Antagonista: {pelicula_menos_vista['antagonista']}")
    print(f"Director: {pelicula_menos_vista['director']}")
    print(f"Género: {pelicula_menos_vista['genero']}")
    print(f"Año: {pelicula_menos_vista['año']}")
    print(f"Visualizaciones: {pelicula_menos_vista['vistas']}")
    print("")
    a = input("Presione ENTER para continuar...")
    limp_pantalla()

    print("\nPromedio de visualizaciones:", promedio_vistas)
    print("")
    a = input("Presione ENTER para continuar...")
    limp_pantalla()
    print("\nCantidad de películas de acción:", contador_accion)
    print("")
    a = input("Presione ENTER para continuar...")
if __name__ == "__main__":
    main()