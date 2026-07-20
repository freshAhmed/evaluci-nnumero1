#clase factura cliente
class Factura_Cliente:
    cliente = ""
    monto = 0.0
    numero_factura = 0
    fecha = ""
    estado_pago = ""
    #metodo constructor
    def __init__(self, cliente, numero_factura, monto = None,  fecha = None, estado_pago = None):
        self.cliente = cliente
        self.numero_factura = numero_factura
        if monto is not None:
            self.monto = monto 
        if fecha is not None:
            self.fecha = fecha
        if estado_pago is not None:
            self.estado_pago = estado_pago
    
    #metodo get para el atributo cliente
    def get_cliente(self):
        return self.cliente
    #metodo get para el atributo numero_factura
    def get_numero_factura(self):
        return self.numero_factura
    #metodo get para el atributo monto
    def get_monto(self):
        return self.monto   
    #metodo get para el atributo fecha
    def get_fecha(self):
        return self.fecha
    #metodo get para el atributo estado_pago
    def get_estado_pago(self):
        return self.estado_pago
    #metodo set para el atributo cliente
    def set_cliente(self, cliente):
        self.cliente = cliente
    #metodo set para el atributo numero_factura
    def set_numero_factura(self, numero_factura):
        self.numero_factura = numero_factura
    #metodo set para el atributo monto
    def set_monto(self, monto):
        self.monto = monto
    #metodo set para el atributo fecha
    def set_fecha(self, fecha):
        self.fecha = fecha
    #metodo set para el atributo estado_pago
    def set_estado_pago(self, estado_pago):
        self.estado_pago = estado_pago

    #mostrar factura
    def mostrar_factura(self):
        cliente = self.cliente
        numero_factura = self.numero_factura
        monto = self.monto
        fecha = self.fecha
        estado_pago = self.estado_pago
        return f"Cliente: {cliente}, Número de factura: {numero_factura}, Monto: {monto}, Fecha: {fecha}, Estado de pago: {estado_pago}"

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