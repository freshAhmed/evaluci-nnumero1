#Menu Principal
while True:
    print("Menu Principal Jaguar")
    print("1. Registro de Clientes")
    print("2. Facturacion")
    print("3. Gestión el estado de pagos")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("Has seleccionado la Opcion 1")
        # Lógica para la Opcion 1
    elif opcion == "2":
        print("Has seleccionado la Opcion 2")
        # Lógica para la Opcion 2
    elif opcion == "3":
        print("Has seleccionado la Opcion 3")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida. Por favor, seleccione una opcion valida.")