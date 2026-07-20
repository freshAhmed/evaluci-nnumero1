#Clase Registro de Clientes
class RegistroClientes:
    nombre = ""
    rut = ""
    email = ""
    telefono = ""
    #metodo constructor
    def __init__(self, nombre, rut, email, telefono):
        self.nombre = nombre
        self.rut = rut
        self.email = email
        self.telefono = telefono

#Registro de Clientes
def registrar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    rut = input("Ingrese el RUT del cliente: ")
    email = input("Ingrese el correo electrónico del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")

    cliente = RegistroClientes(nombre, rut, email, telefono)
    print("Cliente registrado exitosamente:")
    print(f"Nombre: {cliente.nombre}")
    print(f"RUT: {cliente.rut}")
    print(f"Email: {cliente.email}")
    print(f"Teléfono: {cliente.telefono}")
    return cliente

#definir diccionario para almacenar los clientes
diccionario = {}

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
        registro_cliente = registrar_cliente()
        diccionario[registro_cliente.rut] = registro_cliente
        print(diccionario)

        # Lógica para la Opcion 1
    elif opcion == "2":
        print("Has seleccionado la Opcion 2")
        # Lógica para la Opcion 2
    elif opcion == "3":
        print("Has seleccionado la Opcion 3")
        # Lógica para la Opcion 3
    elif opcion == "4":
        print("Saliendo del programa...")
        break
        # Lógica para la Opcion 4
    else:
        print("Opcion invalida. Por favor, seleccione una opcion valida.")