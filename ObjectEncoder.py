from pathlib import Path
import json
from Lista import Lista
from VNuevos import Nuevo
from VUsados import Usado

class ObjectEncoder(object):

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
        
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            print("--Archivo guardado correctamente--")
            destino.close()
    #Otra forma de hacerlo
    #def guardarJSONArchivo(self, diccionario, archivo):
    #    try:
    #        with open(archivo, 'w', encoding='utf-8') as destino:
    #            json.dump(diccionario, destino, indent=4)
    #        print("-- Archivo guardado correctamente --")
    #    except IOError:
    #        print("Error al guardar el archivo JSON.")

        
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)
        
    def decodificarDiccionario(self, lista: Lista):
        diccionario = self.leerJSONArchivo('vehiculos.json')
        for elem in diccionario:
            if '__class__' not in elem:
                    print("No se encuentra el diccionario")
            else:
                class_name=elem['__class__']
                class_=eval(class_name)
                if class_name == "Nuevo":
                    atributos = elem['__atributos__']
                    N = class_(**atributos)
                    lista.agregarVehiculo(N)
                elif class_name == "Usado":
                    atributos = elem['__atributos__']
                    U = class_(**atributos)
                    lista.agregarVehiculo(U)   

    def mostrarJson(self,ar):
        # Abre el archivo JSON y carga en datos el contenido
        with open(ar) as archivo:
            datos = json.load(archivo)
        # Muestra los datos de manera legible
        print(json.dumps(datos, indent=4))
        
    #Otra forma de hacerlo
    # def mostrarJson(self):
        # try:
            # # Abre el archivo JSON y carga en datos el contenido
            # with open('NuevosVehiculos.json') as archivo:
                # datos = json.load(archivo)

            # # Muestra los datos de manera legible
            # print(json.dumps(datos, indent=4))
        # except FileNotFoundError:
            # print("El archivo JSON no existe.")
        # except json.JSONDecodeError as e:
            # print("Error al decodificar el archivo JSON:", str(e))

    def agregarJson(self,lista):
        try:
            with open('vehiculos.json', 'r') as archivo:
                datos = json.load(archivo)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            datos = []

        for diccionario in lista:
            datos.append(diccionario)
        
        with open('vehiculos.json', 'w') as archivo:
            json.dump(datos, archivo, indent=4)
