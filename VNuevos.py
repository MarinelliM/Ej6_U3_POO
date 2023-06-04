from Vehiculos import Vehiculo
class Nuevo(Vehiculo):
    __version: str

    def __init__(self, tipo, marca, modelo, puertas, color, preciob,version) -> None:
        super().__init__(tipo, marca, modelo, puertas, color, preciob)
        self.__version = version

    def importe(self):
        importe = super().importe()
        pat = (importe*10)/100
        full = 0
        if self.__version == 'full':
            full = (importe*2)/100
        suma = (importe+pat+full)
        return suma
    
    def toJson(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                        tipo = self.gettipo(),
                        marca = self.getmarca(), 
                        modelo = self.getmodelo(),
                        puertas = self.getcp(),
                        color = self.getcolor(),
                        precio_base = self.getprecio(),
                        version = self.__version
                  
                    )
            )
        return d

    def mostrarimporte(self):
        print('Importe:')
        print(f'{super().mostrarimporte()}')
    
    def mostrar(self):
        print('Vehiculo Nuevo:')
        print(f'{super().mostrar()}')
        print('Version: {}'.format(self.__version))
