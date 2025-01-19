def Buscar_producto(inventario, Nombre_producto):
    if Nombre_producto in inventario:
        Datos = inventario[Nombre_producto]
        print(f"Producto: {Nombre_producto}")
        print(f"Código: {Datos['Codigo']}")
        if 'Proveedor' in Datos:
            print(f"Proveedor: {Datos['Proveedor']}")
        else:
            print("Proveedor no disponible")
    else:
        print(f"El producto '{Nombre_producto}' no está registrado.")
        print("Productos disponibles en el inventario: ")
        print(list(inventario.keys()))
