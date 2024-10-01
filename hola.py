def calculartotal(cantidadkgs, precioporkg):
    return cantidadkgs * precioporkg

def calcularvuelto(montopagado, totalpagar):
    if montopagado >= totalpagar:
        return montopagado - totalpagar
    else:
        return None

def calcular_nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"

def registrarventas():
    cantidadventas = int(input("Ingrese la cantidad de ventas a realizar: "))
    print("")


    for i in range(cantidadventas):
        print(f"\n--- Venta {i + 1} ---")

        print("")

        nombrevendedor = input("Ingrese el nombre del vendedor: ")
        apellidovendedor = input("Ingrese el apellido del vendedor: ")

        print("")
        print("")

        nombrecliente = input("Ingrese el nombre del cliente: ")
        apellidocliente = input("Ingrese el apellido del cliente: ")

        print("")
        print("")

        cantidadkgs = float(input("Ingrese la cantidad que va a comprar el cliente (en kgs): "))
        producto = input("Ingrese la fruta o verdura que va a comprar el cliente: ")
        precioporkg = float(input(f"Ingrese el precio por kilo de {producto} (en pesos chilenos): "))
        totalpagar = calculartotal(cantidadkgs, precioporkg)
        print(f"Total a pagar: {totalpagar} pesos chilenos")
        montopagado = float(input("Ingrese con cuánto pagó el cliente: "))

        print("")
        print("")


        vuelto = calcularvuelto(monto_pagado, total_a_pagar)

        print("")
        print("")

        print(f"\n--- Resumen de la Venta {i + 1} ---")
        print("")
        print(f"Vendedor: {calcular_nombre_completo(nombrevendedor, apellidovendedor)}")
        print(f"Cliente: {calcular_nombre_completo(nombrecliente, apellidocliente)}")
        print(f"Producto: {producto}")
        print(f"Cantidad comprada: {cantidadkgs} kgs")
        print(f"Total a pagar: {totalpagar} pesos chilenos")

        if vuelto is not None:
            print(f"Vuelto: {vuelto} pesos chilenos")
        else:
            print("El cliente no pagó suficiente dinero.")

registrarventas()