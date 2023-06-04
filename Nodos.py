from Vehiculos import Vehiculo
class Nodo:
    __Vehiculo:Vehiculo
    __siguiente: object

    def __init__(self, vehiculo):
        self.__Vehiculo = vehiculo
        self.__siguiente=None

    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getvehiculo(self):
        return self.__Vehiculo
    
    def getDato(self):
        return self.__Vehiculo.mostrar()
    
    def getTipo(self):
        return self.__Vehiculo.gettipo()
    
    def getpatente(self):
        return self.__Vehiculo.getpatente()
    
    def Mostrarimporte(self):
        return self.__Vehiculo.mostrarimporte()
    
    def getimporte(self):
        return self.__Vehiculo.getimporte()
    
    def setpreciobase(self, precio):
        self.__Vehiculo.setpreciobase(precio)