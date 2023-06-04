class Vehiculo:
    __modelo: str
    __cpuertas: int
    __color: str
    __precio_base: int
    __tipo: str
    __marca: str

    def __init__(self,tipo,marca,modelo,puertas,color,preciob) -> None:
        self.__tipo = tipo
        self.__marca = marca
        self.__modelo = modelo 
        self.__cpuertas = puertas
        self.__color = color
        self.__precio_base = preciob

    def gettipo(self):
        return self.__tipo
    
    def importe(self):
        return self.__precio_base
    
    def getimporte(self):
        importe = self.importe()
        return importe
    
    def getmarca(self):
        return self.__marca
    
    def getmodelo(self):
        return self.__modelo
    
    def getcp(self):
        return self.__cpuertas
    
    def getcolor(self):
        return self.__color
    
    def getprecio(self):
        return self.__precio_base
    
    def getpatente(self):
        pass

    def setpreciobase(self, precio):
        self.__precio_base = precio

    def mostrarimporte(self):
        importe = self.importe()
        return f'{importe}'
    
    # def toJSON(self):
	# 	return {
	# 		'marca': self.__marca,
	# 		'modelo': self.__modelo,
	# 		'color': self.__color,
	# 		'pais': self.__pais,
	# 		'precio': self.__precio
	# 	}
    def toJson(self):
        return 

    def mostrar(self):
        return f'Tipo: {self.__tipo}, Marca: {self.__marca}, Modelo: {self.__modelo}, Color: {self.__color}, Cantidad de puertas: {self.__cpuertas}, Precio Base de venta: {self.__precio_base}' 