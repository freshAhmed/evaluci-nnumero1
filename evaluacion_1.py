import decimal
import re #Regular expression libreria
import time
from decimal import Decimal

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
    Representa una factura de cliente de Jaguar Corp,

    Atributos:

    cliente(str): nombre del cliente
    numero_factura(int): número de factura
    monto(float): monto de la factura
    fecha(str): fecha de la factura
    estado_pago(str): estado de pago de la factura, puede ser "Pagado" o "Pendiente"
    """
    estados_pagos = ["Pagado","Pendiente"]

    #metodo constructor  
    def __init__(self, cliente, numero_factura, monto = 0.0, fecha = "", estado_pago = "Pendiente"):
        """
            Crear una nueva factura de cliente con los atributos especificados.
        
            argumentos:
        
            cliente (str): nombre del cliente
            numero_factura (int): número de factura
            monto (float): monto de la factura, por defecto es 0.0
            fecha (str): fecha de la factura, por defecto es una cadena vacía
            estado_pago (str): estado de pago de la factura, por defecto es "Pendiente"
        
            Raises:
        
            TypeError: si el tipo de dato de alguno de los atributos no es el esperado
            ValueError: si el estado de pago no es "Pagado" o "Pendiente"
        """      
        if not isinstance(cliente, str):
            raise TypeError("El nombre del cliente debe ser una cadena de texto.")
        self.cliente = cliente
        if not isinstance(numero_factura, int):
            raise TypeError("El número de factura debe ser un entero.")
        self.numero_factura = numero_factura
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número decimal.")
        self.monto = monto 
        if not isinstance(fecha, str):
            raise TypeError("La fecha debe ser una cadena de texto.")
        self.fecha = fecha
        if not isinstance(estado_pago, str) or estado_pago not in self.estados_pagos:
            raise ValueError("El estado de pago debe ser 'Pagado' o 'Pendiente'.")
        self.estado_pago = estado_pago
    
    #metodo get para el atributo cliente
    def get_cliente(self):
        """Retornar el nombre del cliente de la factura."""
        return self.cliente
    
    #metodo get para el atributo numero_factura
    def get_numero_factura(self):
        """Retornar el número de factura."""
        return self.numero_factura
    
    #metodo get para el atributo monto
    def get_monto(self):
        """Retornar el monto de la factura."""
        return self.monto   
    
    #metodo get para el atributo fecha
    def get_fecha(self):
        """Retornar la fecha de la factura."""
        return self.fecha
    
    #metodo get para el atributo estado_pago
    def get_estado_pago(self):
        """Retornar el estado de pago de la factura."""
        return self.estado_pago
    
    #metodo set para el atributo cliente
    def set_cliente(self, cliente):
        """Actualizar el nombre del cliente de la factura."""
        if not isinstance(cliente, str):
            raise TypeError("El nombre del cliente debe ser una cadena de texto.")
        self.cliente = cliente

    #metodo set para el atributo numero_factura
    def set_numero_factura(self, numero_factura):
        """Actualizar el número de factura."""
        if not isinstance(numero_factura, int):
            raise TypeError("El número de factura debe ser un entero.")
        self.numero_factura = numero_factura

    #metodo set para el atributo monto
    def set_monto(self, monto):
        """Actualizar el monto de la factura."""
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número decimal.")
        self.monto = monto

    #metodo set para el atributo fecha
    def set_fecha(self, fecha):
        """Actualizar la fecha de la factura."""
        if not isinstance(fecha, str):
            raise TypeError("La fecha debe ser una cadena de texto.")
        self.fecha = fecha

    #metodo set para el atributo estado_pago
    def set_estado_pago(self, estado_pago):
        """Actualizar el estado de pago de la factura."""
        if not isinstance(estado_pago, str) or estado_pago not in self.estados_pagos:
            raise ValueError("El estado de pago debe ser 'Pagado' o 'Pendiente'.")
        self.estado_pago = estado_pago

    #mostrar factura
    def mostrar_factura(self):
        """Retornar una cadena de texto que representa la factura con todos sus atributos."""
        cliente = self.cliente
        numero_factura = self.numero_factura
        monto = self.monto
        fecha = self.fecha
        estado_pago = self.estado_pago
        return f"Cliente: {cliente}, Número de factura: {numero_factura}, Monto: {monto}, Fecha: {fecha}, Estado de pago: {estado_pago}"
    
    def aplicar_descuento(self,porcentaje_del_descuento):
        """Aplica un descuento al monto de la factura según el porcentaje especificado.
        el porcentaje debe ser un número decimal entre 0 y 100.
        raises:
        TypeError: si el porcentaje no es un número decimal"""
        if not isinstance(porcentaje_del_descuento, (int, float)): # validar el porcentaje del descuento
            raise TypeError("El porcentaje del descuento no es valida !!")   
        elif porcentaje_del_descuento > 0 and porcentaje_del_descuento < 100:
          self.monto = self.monto - (self.monto * porcentaje_del_descuento / 100)
          print(f"El nuevo monto {self.monto}$")

    def marcar_pagado(self,dinero_pagado = 0):
       """Marcar la factura como pagada.

       raises:

       TypeError: si el monto pagado no es un número decimal
       ValueError: si el monto pagado no es válido"""
       if not isinstance(dinero_pagado, (int, float, decimal.Decimal)):
          raise TypeError("El monto pagado Ingresado no es valido!! debe ser decimal")
       
       elif dinero_pagado <= 0:
          raise ValueError("El monto pagado Ingresado no es valido!! debe ser mayor de cero")
          
       
       self.set_estado_pago("Pagado")  

#Crear factura de cliente
def crear_factura(cliente):
    """Crear una nueva factura de cliente con los atributos especificados.

    raises:

    TypeError: si el tipo de dato de alguno de los atributos no es el esperado
    ValueError: si el número de factura no es un entero o si el monto no es un número decimal"""
    nombrecliente = cliente.nombre
    try:
        numero_factura = int(input("Ingrese el número de factura: "))
    except ValueError:
        print("Error: El número de factura debe ser un entero.")
        return None
    try:
         monto = float(input("Ingrese el monto de la factura: "))

    except ValueError:
        print("Error:El monto debe ser un número decimal.")
        return None

    fecha = gettime()
    factura = Factura_Cliente(nombrecliente, numero_factura, monto, fecha)
    print("Factura creada exitosamente:")
    print(factura.mostrar_factura())
    return factura

#Clase Registro de Clientes
class Cliente:

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

    cliente = Cliente(nombre, rut, email, telefono) if not (rut in dict.keys(registro_de_clientes)) else registro_de_clientes.get(rut)

    print("Cliente registrado exitosamente:")
    print(f"Nombre: {cliente.nombre}")
    print(f"RUT: {cliente.rut}")
    print(f"Email: {cliente.email}")
    print(f"Teléfono: {cliente.telefono}")
    return cliente

#gestión el estado de pago
def gestionar_estado_pago():


    print("1. Marcar como pagada")
    print("2. Descuento")
    print("3. mostrar lista de facturas del cliente")
    print("4. salir")
    opcion = int(input("Seleccione una opción: "))

    
    if opcion == 1:
     rut = str(input("Ingrese el RUT del cliente: "))
     while not veríficar_el_rut(rut): 
      print(f"El Rut {rut} Ingresado no es valido !!")
      rut = str(input("Ingrese el RUT del cliente: ")) 

     cliente = registro_de_clientes.get(rut)
     if not cliente:
        print("Cliente no encontrado.")
        return
     
     
     try:
        numero_factura = int(input("Ingrese el número de factura: "))
        factura = cliente.registro_de_facturas.get(numero_factura)
        if not factura:
            print("Factura no encontrada.")
            return
        
     except ValueError:
        print("Error: El número de factura debe ser un entero.")
        return
     print(f"Estado actual de la factura: {factura.get_estado_pago()}")

     if factura.get_estado_pago() == "Pagado":
             print("La factura ya está marcada como pagada.")
             return
     try:
           dinero_pagado=Decimal(input(f"Ingrese el monto pagado: debe ser mayor de zero y igual al monto de la factura {factura.get_monto()}$ "))

     except ValueError:
      print("Error:El monto pagado debe ser un numero decimal.")
      return
        
     factura.marcar_pagado(dinero_pagado)
     print(f"Estado actualizado de la factura: {factura.get_estado_pago()}")
    elif opcion == 2:
     rut = str(input("Ingrese el RUT del cliente: "))
     while not veríficar_el_rut(rut): 
      print(f"El Rut {rut} Ingresado no es valido !!")
      rut = str(input("Ingrese el RUT del cliente: ")) 

     cliente = registro_de_clientes.get(rut)
     if not cliente:
      print("Cliente no encontrado.")
      return

     try:
        numero_factura = int(input("Ingrese el número de factura: "))
        factura = cliente.registro_de_facturas.get(numero_factura)
        if not factura:
            print("Factura no encontrada.")
            return
     except ValueError:
        print("Error: El número de factura debe ser un entero.")
        return
     try:
            porcentaje = float(input("Ingrese el porcentaje de descuento: "))
            factura.aplicar_descuento(porcentaje)
     except ValueError:
       print("Error: El porcentaje de descuento debe ser un número decimal.")
   
   

    elif opcion == 3:
      rut = str(input("Ingrese el RUT del cliente: "))
      while not veríficar_el_rut(rut): 
        print(f"El Rut {rut} Ingresado no es valido !!")
        rut = str(input("Ingrese el RUT del cliente: "))   
      cliente = registro_de_clientes.get(rut)
      if not cliente:
        print("Cliente no encontrado.")
        return
      print("Lista de facturas del cliente:")
      for factura in cliente.registro_de_facturas.values():
        print("|-------------------------|")
        print(factura.mostrar_factura())

    elif opcion == 4:
        print("Saliendo de la gestión de pagos...")
        return
    else:
        print("Opción inválida.")
        
#definir diccionario para almacenar los clientes
registro_de_clientes = {}


#Menu Principal
def menu_principal():
 while True:
    print("Menu Principal Jaguar")
    print("1. Registro de Clientes")
    print("2. Facturacion")
    print("3. Gestión el estado de pagos")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1": # Registro de Clientes
        print("Has seleccionado la Opcion 1")
        cliente = registrar_cliente()
        registro_de_clientes[cliente.rut] = cliente
        print("El cliente fue registrado !!")
        # Lógica para la Opcion 1
    elif opcion == "2": # crear Nueva factura
        print("Has seleccionado la Opcion 2")
        rut=str(input("ingresa el Rut del cliente: "))
        while not veríficar_el_rut(rut): 
          print(f"El Rut {rut} Ingresado no es valido !!")
          rut = str(input("Ingrese el RUT del cliente: ")) 
        cliente=registro_de_clientes.get(rut)
        if not cliente:
          print("Cliente no encontrado.")
        factura = crear_factura(cliente) if cliente is not None else None
        if factura is not None:
            cliente.registro_de_facturas[factura.get_numero_factura()] = factura
    
        # Lógica para la Opcion 2
    elif opcion == "3": # gestión el estado de pago
        print("Has seleccionado la Opcion 3")
        gestionar_estado_pago()
        # Lógica para la Opcion 3
    elif opcion == "4": # salir
        print("Saliendo del programa...")
        break
        # Lógica para la Opcion 4
    else:
        print("Opcion invalida. Por favor, seleccione una opcion valida.")
 
if __name__== "__main__":
    """
    realizar las pruebas del sistema aquí !!! 
   """
    print("Prueba del sistema de facturación de Jaguar Corp ")

    #instancias con parametros obligatorios
    print("Creando instancias de Factura_Cliente con parámetros obligatorios...")
    factura1 = Factura_Cliente("Juan Perez", 1001)
    print(factura1.mostrar_factura())

    #instancias con todos los parametros
    print("Creando instancias de Factura_Cliente con todos los parámetros...")
    factura2 = Factura_Cliente("Maria Gonzalez", 1002, 1500.75, "2024-06-01 10:30:00", "Pendiente")
    print(factura2.mostrar_factura())

    #Descuento positivo valido(entre 0 y 100)
    print("Aplicando descuento válido a la factura2...")
    factura2.aplicar_descuento(10)
    print(factura2.mostrar_factura())

    #Descuento negativo invalido o mayor a 100
    print("Intentando aplicar descuento inválido a la factura2...")
    factura2.aplicar_descuento(150)  # Esto debería generar un error
    print(factura2.mostrar_factura())

    #marcar como pagado con monto valido
    print("Marcando factura2 como pagada con monto válido...")
    factura2.marcar_pagado(1500.75)
    print(factura2.mostrar_factura())

    #marcar como pagado con monto invalido o igual a cero
    print("Intentando marcar factura2 como pagada con monto inválido...")
    try:
        factura2.marcar_pagado(0)  # Esto debería generar un error
    except ValueError as error:
        print(f"Error: {error}")
    print(factura2.mostrar_factura())

    #uso del metodo get y set para actualizar el nombre del cliente, estado de pago, monto y fecha de la factura
    print("actualizando el nombre del cliente de la factura1...")
    print(f"cliente antes de la actualización: {factura1.get_cliente()}")
    factura1.set_cliente("Juan Perez Actualizado")
    print(f"cliente despues de la actualización: {factura1.get_cliente()}")

    print("Estado de pago antes de la actualización: ", factura1.get_estado_pago())
    factura1.set_estado_pago("Pagado")
    print("Estado de pago después de la actualización: ", factura1.get_estado_pago())

    print("Monto de la factura antes de la actualización: ", factura1.get_monto())
    factura1.set_monto(2000.50)
    print("Monto de la factura después de la actualización: ", factura1.get_monto())

    print("Fecha de la factura antes de la actualización: ", factura1.get_fecha())
    factura1.set_fecha("2024-06-02 12:00:00")
    print("Fecha de la factura después de la actualización: ", factura1.get_fecha())

    menu_principal()