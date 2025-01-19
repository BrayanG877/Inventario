from datetime import datetime

def Retirar_producto(inventario, Nombre_producto, Cantidad, Bodega, Descripcion):
    if Nombre_producto in inventario:
        if Bodega in inventario[Nombre_producto]["BODEGAS"]:
            if inventario[Nombre_producto]["BODEGAS"][Bodega] >= Cantidad:
                inventario[Nombre_producto]["BODEGAS"][Bodega] -= Cantidad
                Fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                operacion = {
                    "Tipo": "Salida",
                    "Cantidad": Cantidad,
                    "Bodega": Bodega,
                    "Fecha": Fecha_hora,
                    "Descripcion": Descripcion
                }
                inventario[Nombre_producto]['Historial'].append(operacion)
                print(f"Se han retirado {Cantidad} unidades de '{Nombre_producto}' en la bodega '{Bodega}'.")
            else:
                print(f"No hay suficiente stock en la bodega '{Bodega}' para retirar {Cantidad} unidades.")
        else:
            print(f"La bodega '{Bodega}' no es válida.")
    else:
        print(f"El producto '{Nombre_producto}' no está registrado en el inventario.")
