from Vehiculos import Vehiculo
class Usado(Vehiculo):
    __patente:str
    __año:int 
    __kilometraje:int

    def __init__(self, tipo, marca, modelo, puertas, color, preciob,patente,año,kilometraje) -> None:
        super().__init__(tipo, marca, modelo, puertas, color, preciob)
        self.__patente = patente
        self.__año = año
        self.__kilometraje = kilometraje

    def getpatente(self):
        return self.__patente
    
    def mostrarimporte(self):
        importe = super().mostrarimporte()
        return print(f'Importe de venta/Precio de venta: {importe}')
    
    #menos el 1% por cada año de antigüedad 
    #(año actual – año del vehículo), menos el 2% si el kilometraje supera los 100.000. 
    #Ambos porcentajes se calculan sobre el precio base.
    def importe(self):
        km = 0
        importe = super().importe()
        añoa = (2023 - self.__año)
        años = (añoa*importe)/100
        if self.__kilometraje > 100000:
            km = (importe*2)/100
        resta = importe - km - años
        return resta
    
    def toJson(self):
        dato = super().toJson()
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                        tipo = self.gettipo(),
                        marca = self.getmarca(), 
                        modelo = self.getmodelo(),
                        puertas = self.getcp(),
                        color = self.getcolor(),
                        precio_base = self.getprecio(),
                        patente = self.__patente,
                        anio = self.__año,
                        kilometraje = self.__kilometraje
                    )
            )
        return d

    def mostrar(self):
        print('Vehiculo Usado:')
        print(f'{super().mostrar()}')
        print('Patente: {}, Año del Vehiculo: {}, Kilometraje: {}'.format(self.__patente,self.__año,self.__kilometraje))
