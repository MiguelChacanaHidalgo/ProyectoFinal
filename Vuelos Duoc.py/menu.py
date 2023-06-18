import funciones as fn

while True:
  try:
   print("Menú Principal")
   print("1. Ver asientos disponibles")
   print("2. Comprar asiento")
   print("3. Anular vuelo")
   print("4. Modificar datos de pasajero")
   print("5. Salir")
   opcion = int(input("Ingrese una opción: "))
  except:
   print("DEBE INGRESAR UNA DE LAS OPCIONES")

  try:
    if opcion == 1:
          fn.mostrar_asientos()
    elif opcion == 2:
          fn.comprar_asiento()
    elif opcion == 3:
          fn.anular_vuelo()
    elif opcion == 4:
          fn.modificar_datos()
    elif opcion == 5:
          print("¡Gracias por utilizar nuestro sistema de venta de pasajes vuelva pronto!")
          break
    else:
          print("Opción inválida.")
  except:
    print()
