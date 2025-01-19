import json
from time import sleep
def Cargar_Inventario():
    try:
        with open ("Inventario.json","r")as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo 'Inventario' No existe. Creando inventario vacio..")
        sleep(5)
        return {}
