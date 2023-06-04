from Vehiculos import Vehiculo
from Lista import Lista
from Lista import CInterface
from ObjectEncoder import ObjectEncoder
from VNuevos import Nuevo
from VUsados import Usado
if __name__ == '__main__':
        lista = Lista()
        interfaz = CInterface(lista)
        vehiculo1 = Usado('Usado','Ford','F100',2,'blanco', 10000000,'ABC-490',1990,1000000)
        vehiculo2 = Nuevo('Nuevo','Volskwagen','Vento',4,'gris', 45000000,'full')
        posicion = int(input('Ingrese la posicion donde quiere almacenar al objeto en la lista:'))
        lista.agregarVehiculo(vehiculo1)
        lista.mostrar()
        lista.insertarVehiculo(vehiculo2,posicion)
        lista.mostrar()
        lista.mostrarVehiculo()

        a = input('De aqui en adelante se hace Prueba de la Interfaz:')
        vehiculo3 = Usado('Usado','Ford','F150',2,'blanco', 1000,'AFC-321',1990,1000)
        interfaz.agregarVehiculo(vehiculo3)
        lista.mostrar()
        vehiculo4 = Nuevo('Nuevo','Volskwagen','Amarok',4,'gris', 998238422,'full')
        posicion = int(input('Ingrese la posicion donde quiere almacenar al objeto en la lista:'))
        interfaz.insertarVehiculo(vehiculo4,posicion)
        lista.mostrar()
        a = input('valor:')
        interfaz.mostrarVehiculo()
        
        print('Inciso 4:')
        lista.buscarXpatente()

        a = input('Inciso 5:')
        lista.vehiculomaseco()

        a = input('Inciso 7:')
        # OE = ObjectEncoder()
        # l = lista.almacenaJson()
        
        # OE.guardarJSONArchivo(l, "NuevosVehiculos.json")
        # a = input('Mostrar archivo json cargado con la lista definida:')
        # OE.mostrarJson()

        # Crear una instancia de ObjectEncoder
        OE = ObjectEncoder()

        # Guardar la lista de vehículos en formato JSON
        l = lista.almacenaJson()
        OE.guardarJSONArchivo(l, "NuevosVehiculos.json")

        a = input('Mostrar archivo JSON cargado con la lista definida:')
        OE.mostrarJson('NuevosVehiculos.json')


        print('De aqui en adelante se trabaja con los archivos json')
        print('Si continua se modificara el archivo json')
        a = int(input('Si quiere continuar ingrese 1 para SI o 0 para NO:'))
        while a != 0:
                if a == 1:
                        jsonF = ObjectEncoder()
                        objeto2 = Nuevo("Nuevo", "Toyota", "corolla", 4, "blanco", 120000000, "full")
                        objeto3 = Usado("Usado","Chevrolet", "Trucker", 4, "gris", 50000000, "AF-523-BA", 2020, 20000)
                        d1 = objeto2.toJson()
                        d2 = objeto3.toJson()
                        lista = [d1, d2]
                        jsonF.agregarJson(lista)
                        #La funcion guardar, reemplaza en el archivo la informacion cargada por una nueva que le enviamos
                        #jsonF.guardarJSONArchivo(lista, "vehiculos.json")
                        
                        jsonF.mostrarJson()
                else: a = int(input('Opcion invalida, Si quiere continuar ingrese 1 para SI o 0 para NO:'))
