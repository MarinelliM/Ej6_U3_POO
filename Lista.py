from VNuevos import Nuevo
from VUsados import Usado
from Nodos import Nodo
from zope.interface import implementer,IInterfaceDeclaration
class CInterface(IInterfaceDeclaration):
    def insertarVehiculo(self, vehiculo, posicion):
        pass
    def agregarVehiculo(self, vehiculo):
        pass
    def mostrarVehiculo(self):
        pass

@implementer(CInterface)
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__tope = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
        
    def agregarVehiculo(self, vehiculo):
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    
    # def insertarVehiculo(self,vehiculo,posicion):
    #     i = 1
    #     aux = self.__comienzo
    #     if posicion < 0 or posicion > self.__tope:
    #             raise Exception('La posicion no es valida')
    #     else:
    #         while i <= self.__tope:
    #             if posicion == 0:
    #                 self.agregarVehiculo(vehiculo)
    #                 i = 1+self.__tope
    #             elif posicion == 1:
    #                 nodo = Nodo(vehiculo)
    #                 aux.setSiguiente(nodo)
    #                 i = self.__tope+1
    #             elif i != posicion:
    #                 aux = aux.getSiguiente()
    #                 i+=1
    #             elif i == posicion:
    #                 nodo = Nodo(vehiculo)
    #                 nodo.setSiguiente(aux)
    #                 self.__actual = nodo
    #                 i = self.__tope+1
    #         self.__tope+=1

    def insertarVehiculo(self,vehiculo,posicion):
        i = 0
        aux = self.__comienzo
        if posicion < 0 or posicion > self.__tope:
                raise Exception('La posicion no es valida')
        else:
            
            if posicion == 0:
                self.agregarVehiculo(vehiculo)
                i = posicion
            
            while i < posicion-1:
                aux = aux.getSiguiente()
                i += 1
            nodo = Nodo(vehiculo)
            nodo.setSiguiente(aux.getSiguiente())
            aux.setSiguiente(nodo)
            #Se verifica si la posición es igual a la última posición.
            # Si es así, se actualiza la referencia al nodo actual
            # para que apunte al nuevo nodo, ya que el nuevo nodo ha sido insertado en la última posición.
            if posicion == self.__tope:
                self.__actual = nodo        
            self.__tope+=1

    def mostrar(self):
        aux = self.__comienzo
        for e in range(self.__tope):
            if aux != None:
                aux.getDato()
                aux = aux.getSiguiente()
            else: 
                return print('Fin de la lista')
            

    def mostrarVehiculo(self):
        posicion = int(input('Ingrese la posicion del nodo que quiere ver:'))
        if posicion < 0 or posicion > self.__tope:
                raise Exception('La posicion no es valida')
        else:
            nodo = self.buscarnodo(posicion)
            print('Objeto:')
            nodo.getDato()
            nodo.Mostrarimporte()

    def buscarnodo(self,pos):
        actual = self.__comienzo
        while actual != None and pos != 0:
            actual = actual.getSiguiente()
            pos -= 1
        if actual == None:
            raise Exception("Posicion invalida")
        return actual
    
    def buscarXpatente(self):
        patente = str(input('Ingrese la patente a buscar:'))
        i = 0
        aux = self.__comienzo
        while i < self.__tope:
            tipo = aux.getTipo()
            if tipo == 'Usado' and patente == aux.getpatente():
                precio = int(input('Ingrese el nuevo precio base del vehiculo:'))
                aux.setpreciobase(precio)
                aux.Mostrarimporte()
                i = self.__tope
            else: 
                aux = aux.getSiguiente()
                i += 1

    def vehiculomaseco(self):
        i = 0
        a = 0
        aux = self.__comienzo
        min = 10000000000000000
        while i < self.__tope:
            importe = aux.getimporte()
            if importe < min:
                min = importe
                aux = aux.getSiguiente()
                i+=1
            else: 
                aux = aux.getSiguiente()
                i+=1 
        aux = self.__comienzo
        while a < self.__tope:
            importe = aux.getimporte()
            if importe == min:
                print('Vehiculo mas economico:')
                aux.getDato()
                print(f'Importe: {importe}')
                a = self.__tope
            else: 
                aux = aux.getSiguiente()
                a+=1
    
    def almacenaJson(self):
        #OE = ObjectEncoder()
        lista = []
        aux = self.__comienzo
        while aux is not None:
            vehiculo = aux.getvehiculo()
            if isinstance(vehiculo, Nuevo):
                dicc = vehiculo.toJson()
            elif isinstance(vehiculo, Usado):
                dicc = vehiculo.toJson()
            else:
                raise ValueError('Tipo de vehículo no válido')

            lista.append(dicc)
            aux = aux.getSiguiente()
            print(lista)
        return lista
