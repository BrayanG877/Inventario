from time import sleep

def Cargar_Inventario():
    try:
        with open("Inventario.json", "r") as archivo:
            contenido = archivo.read().strip()  
            if not contenido:  
                print("El archivo 'Inventario.json' está vacío. Se cargará un inventario vacío.")
                return {}
            return json.loads(contenido)  
    except FileNotFoundError:
        print("El archivo 'Inventario.json' no existe. Creando inventario vacío...")  
        sleep(5)  
        return {} 
    except json.JSONDecodeError:
        print("Error al leer el archivo 'Inventario.json'. El archivo está mal formado.")
        return {}
