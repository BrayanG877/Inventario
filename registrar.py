def Registrar_producto(inventario, Codigo_producto,Nombre_producto,Proveedor_producto):
    if Nombre_producto in inventario:
        print(f"El Producto '{Nombre_producto}' Ya esta registrad.")
    else:
        inventario[Nombre_producto]= {
            "Nombre": Nombre_producto,
            "Codigo" : Codigo_producto,
            "Proveedor" : Proveedor_producto,
            "Bodegas" : {"Norte":0,"Centro":0,"Oriente":0},
            "Historial": []
        }
        print(f"Producto '{Nombre_producto}' ha sido registrado correctamente.")
        print(inventario[Nombre_producto]) 
