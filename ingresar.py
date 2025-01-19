from datetime import datetime

def Ingresar_producto(inventario, Nombre_producto, Cantidad, Bodega):
    if Nombre_producto in inventario:
        if Bodega in inventario[Nombre_producto]["Bodegas"]:
            inventario[Nombre_producto]["Bodegas"][Bodega] += Cantidad
            Fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
            operacion = {
                "Tipo": "Entrada",
                "Cantidad": Cantidad,
                "Bodega": Bodega,
                "Fecha": Fecha_hora,
                "Descripcion": "Ingreso al inventario"
            }
            inventario[Nombre_producto]['Historial'].append(operacion)
            print(f"Se han ingresado {Cantidad} unidades de {Nombre_producto} en la Bodega '{Bodega}'.")
        else:
            print(f"La Bodega '{Bodega}' no es válida. Las bodegas disponibles son: Norte, Centro, Oriente.")
    else:
        print(f"El producto '{Nombre_producto}' no está registrado en el inventario.")
