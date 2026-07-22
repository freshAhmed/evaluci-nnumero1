class Factura_Cliente:
    """
    clase de facturación 
    """
    cliente = ""
    monto = 0.0
    numero_factura = 0
    fecha = ""
    estados_pagos = ["Pagado","Pendiente"]

    #metodo constructor
    def __init__(self, cliente, numero_factura, monto = 0.0, fecha = "", estado_pago = "Pendiente"):
        self.cliente = cliente
        self.numero_factura = numero_factura
        self.monto = monto 
        self.fecha = fecha
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
    
    def aplicar_descuento(self,porcentaje_del_descuento):
        if not isinstance(porcentaje_del_descuento, (int, float)): # validar el porcentaje del descuento
            raise Exception("El porcentaje del descuento no es valida !!")   
        elif porcentaje_del_descuento>0 and porcentaje_del_descuento<100:
          self.monto = self.monto - (self.monto * porcentaje_del_descuento / 100)
          print(f"El nuevo monto {self.monto}$")

    def marcar_pagado(self):
       
       if not isinstance(self.monto, (int, float)):
          raise Exception("El monto Ingresado no es valido!! debe ser decimal")
       
       elif self.monto<=0:
          print("El monto Ingresado no es valido!! debe ser mayor de zero")
          return
          
       self.set_estado_pago("Pagado")  

#Crear factura de cliente
def crear_factura():
    cliente = input("Ingrese el nombre del cliente: ")
    numero_factura = int(input("Ingrese el número de factura: "))
    monto = float(input("Ingrese el monto de la factura: "))
    fecha = input("Ingrese la fecha de la factura (YYYY-MM-DD): ")
    
    factura = Factura_Cliente(cliente, numero_factura, monto, fecha)
    print("Factura creada exitosamente:")
    print(factura.mostrar_factura())
    return factura

#Clase Registro de Clientes
class RegistroClientes:
    nombre = ""
    rut = ""
    email = ""
    telefono = ""
    #metodo constructor
    def __init__(self, nombre="", rut="", email="", telefono=""):
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
diccionario_facturas = {}

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
        factura = crear_factura()
        diccionario_facturas[factura.get_numero_factura()] = factura
        print(diccionario_facturas)
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
    # una idea para mejorar el sistema es cuando el usario elegio opción distento de la opción de salir y despues realizar el opción elegido, el sistema debe entrar en modo de dormir y cuando usario toca cualquier button del teclado para que se despierta  #
    #agregar un opción para mostrar las clientes en la base de datos y filtrar usando nombre o rut #


if __name__== "__main__":
    """
    realizar las pruebas del sistema aquí !!! 
    """
    factura = Factura_Cliente("Juan Perez", 12345, 100.0, "2023-06-01", "Pendiente")
    print(factura.mostrar_factura())
    factura.aplicar_descuento(10)
    factura.marcar_pagado()
    print(factura.mostrar_factura())
d = {1: "a", 2: "b"}
print(d.get(1))
print(d.get(99))