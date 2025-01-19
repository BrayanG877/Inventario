def Historial_producto(inventario, Nombre_producto):
    if Nombre_producto in inventario:
        Datos = inventario[Nombre_producto]
        print(f"\nHistorial de '{Nombre_producto}':")
        for operacion in Datos['Historial']:
            print(f"Fecha: {operacion['Fecha']}, Tipo:{operacion['Tipo']}, Cantidad:{operacion['Cantidad']}, Bodega: {operacion['Bodega']}, Descripcion:{operacion['Descripcion']}")
    else:
        print(f"El producto '{Nombre_producto}' No esta registrado.")
