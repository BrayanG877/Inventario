import json

def Guardar_inventario(inventario):
    with open("Inventario.json","w") as archivo:
        json.dump(inventario, archivo, indent=4)
    print("Inventario guardado correctamente!.")
