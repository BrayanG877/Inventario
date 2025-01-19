def Buscar_producto(inventario, Nombre_producto):
    if Nombre_producto in inventario:
        Datos = inventario[Nombre_producto]
        print(f"\nProducto: {Nombre_producto}")
        print(f"Codigo: {Datos['Codigo']}")
        print(f"Proveedor: {Datos['Proveedor']}") 
        for Bodega, Cantidad in Datos['Bodegas'].items():
            print(f"Cantidad en Bodega {Bodega}: {Cantidad}")
        else:
            print(f"El producto '{Nombre_producto}' No esta registrado.")
