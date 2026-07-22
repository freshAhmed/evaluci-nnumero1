import re #Regular expression libreria
import time
def veríficar_el_rut(rut):
    #verifícar el Rut ingresado por la cliente 
    regxrut=r"^\d{7,8}-?[0-9Kk]$"
    return True if re.match(regxrut,rut) is not None else False 

def veríficar_el_correo(email):
    regxemail=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return True if re.match(regxemail,email) is not None else False 

def veríficar_el_telefono(telefono):
 regxtelefono=r"^(\+56)?9\d{8}"
 return True if re.match(regxtelefono,telefono) is not None else False

def gettime():
    tiempo_estractura=time.gmtime()
    return str(time.strftime("%Y-%m-%d %H:%M:%S",tiempo_estractura))  
    

class Factura_Cliente:
    """
    clase de facturación 
    """

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
def crear_factura(cliente):
    nombrecliente = cliente.nombre
    numero_factura = int(input("Ingrese el número de factura: "))
    monto = float(input("Ingrese el monto de la factura: "))
    fecha = gettime()
    
    factura = Factura_Cliente(nombrecliente, numero_factura, monto, fecha)
    print("Factura creada exitosamente:")
    print(factura.mostrar_factura())
    return factura

#Clase Registro de Clientes
class RegistroClientes:

    #metodo constructor
    def __init__(self, nombre="", rut="", email="", telefono=""):
        self.nombre = nombre
        self.rut = rut
        self.email = email
        self.telefono = telefono
        self.registro_de_facturas={} 
#Registro de Clientes
def registrar_cliente():
    nombre = str(input("Ingrese el nombre del cliente: "))
    rut = str(input("Ingrese el RUT del cliente: ")) 
    while not veríficar_el_rut(rut): 
      print(f"El Rut {rut} Ingresado no es valido !!")
      rut = str(input("Ingrese el RUT del cliente: ")) 

    email = str(input("Ingrese el correo electrónico del cliente: "))
    while not veríficar_el_correo(email):
     print(f"El correo {email} Ingresado no es valido!!")
     email = str(input("Ingrese el correo electrónico del cliente: "))
     
    telefono = str(input("Ingrese el número de teléfono del cliente: "))
    while not veríficar_el_telefono(telefono):
       print(f"el telefono Ingresado no es valido!!")
       telefono = str(input("Ingrese el número de teléfono del cliente: "))

    cliente = RegistroClientes(nombre, rut, email, telefono) if not (rut in dict.keys(registro_cliente)) else registro_cliente[rut]

    print("Cliente registrado exitosamente:")
    print(f"Nombre: {cliente.nombre}")
    print(f"RUT: {cliente.rut}")
    print(f"Email: {cliente.email}")
    print(f"Teléfono: {cliente.telefono}")
    return cliente

#definir diccionario para almacenar los clientes
registro_de_clientes = {}
diccionario_facturas = {}

#Menu Principal
while True:
    print("Menu Principal Jaguar")
    print("1. Registro de Clientes")
    print("2. Facturacion")
    print("3. Gestión el estado de pagos")
    print("4. Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == "1": # Registro de Clientes
        print("Has seleccionado la Opcion 1")
        registro_cliente = registrar_cliente()
        print(f"Nombre : {registro_cliente.nombre}\n Rut:{registro_cliente.rut}\n Email:{registro_cliente.email}\n Teléfono:{registro_cliente.telefono}\n")
        registro_cliente[registro_cliente.rut] = registro_cliente
        print("El cliente fue registrado !!")


        # Lógica para la Opcion 1
    elif opcion == "2": # crear Nueva factura
        print("Has seleccionado la Opcion 2")
        rut=str(input("ingresa el Rut del cliente"))
        while not veríficar_el_rut(rut): 
          print(f"El Rut {rut} Ingresado no es valido !!")
          rut = str(input("Ingrese el RUT del cliente: ")) 
        
        factura = crear_factura()
        diccionario_facturas[factura.get_numero_factura()] = factura
        print(diccionario_facturas)
        # Lógica para la Opcion 2
    elif opcion == "3": # gestión el estado de pago
        print("Has seleccionado la Opcion 3")
        # Lógica para la Opcion 3
    elif opcion == "4": # salir
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
#     factura = Factura_Cliente("Juan Perez", 12345, 100.0, "Pendiente")
#     print(factura.mostrar_factura())
#     factura.aplicar_descuento(10)
#     factura.marcar_pagado()
#     print(factura.mostrar_factura())
# d = {1: "a", 2: "b"}
# print(d.get(1))
# print(d.get(99))