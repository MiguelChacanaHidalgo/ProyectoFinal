asientos = [[0] * 6 for _ in range(7)]

def mostrar_asientos():
    print("Asientos disponibles:")
    for i in range(len(asientos)):
        for c in range(len(asientos[i])):
            if asientos[i][c] == 0:
                print(i * 6 + c + 1, end=" ")
            else:
                print("X", end=" ")
        print()
    print()

def comprar_asiento():
    while True:
        try:
          nom_pasajero = str(input("Ingrese el nombre del pasajero: "))
          break
        except:
          print("INGRESE NOMBRE SIN NUMEROS")
    while True:
        try:
          rut_pasajero = int(input("Ingrese el RUT del pasajero: "))
          break
        except:
          print("INGRESE VALORES NUMERICOS")
    while True:
        try:
          telefono_pasajero = int(input("Ingrese el teléfono del pasajero: "))
          break
        except:
          print("INGRESE VALORES NUMERICOS")
    while True:
        try:
          banco_pasajero = str(("Ingrese el banco del pasajero: "))
          break
        except:
          print("INGRESE NOMBRE SIN NUMEROS")


    mostrar_asientos()
    asiento = int(input("Seleccione el número de asiento que desea comprar: "))

    if asiento < 1 or asiento > 42 or asientos[(asiento - 1) // 6][(asiento - 1) % 6] != 0:
        print("El asiento seleccionado no está disponible.")
        return

    if asiento >= 31:
        precio = 240000
    else:
        precio = 78900

    if banco_pasajero.lower() == "bancoduoc":
        precio -= precio * 0.15

    asientos[(asiento - 1) // 6][(asiento - 1) % 6] = 1

    print("Asiento comprado con éxito.")
    print("Nombre del pasajero:", nom_pasajero)
    print("RUT del pasajero:", rut_pasajero)
    print("Teléfono del pasajero:", telefono_pasajero)
    print("Banco del pasajero:", banco_pasajero)
    print("Precio del pasaje:", precio)
    print()

    def anular_vuelo():
    asiento = int(input("Ingrese el número de asiento que desea anular: "))

    if asiento < 1 or asiento > 42 or asientos[(asiento - 1) // 6][(asiento - 1) % 6] == 0:
        print("El asiento seleccionado no está ocupado.")
        return

    asientos[(asiento - 1) // 6][(asiento - 1) % 6] = 0
    print("Asiento anulado con éxito.")
    print()

def modificar_datos():
    asiento = int(input("Ingrese el número de asiento del pasajero: "))

    if asiento < 1 or asiento > 42 or asientos[(asiento - 1) // 6][(asiento - 1) % 6] == 0:
        print("El asiento seleccionado no está ocupado.")
        return

    rut_pasajero = input("Ingrese el RUT del pasajero para verificar los datos: ")

    if rut_pasajero != "123456789":  
        print("El RUT ingresado no coincide con los datos del pasajero.")
        return

    print("Seleccione el dato que desea modificar:")
    print("1. Nombre del pasajero")
    print("2. Teléfono del pasajero")
    opcion = int(input("Opción: "))

    if opcion == 1:
        nuevo_nombre = input("Ingrese el nuevo nombre del pasajero: ")
        print("Nombre del pasajero actualizado con éxito.")
    elif opcion == 2:
        nuevo_telefono = input("Ingrese el nuevo teléfono del pasajero: ")
        print("Teléfono del pasajero actualizado con éxito.")
    else:
        print("Opción inválida.")

    print()
