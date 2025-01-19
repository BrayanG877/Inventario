def Reporte(inventario):
    print("\nReporte de inventartio:")
    for producto, Datos in inventario.items():
        print(f"\nProducto: {producto}")
        print(f"Nombre: {Datos['Nombre']}")
        print(f"Proveedor: {Datos['Proveedor']}")
        for Bodega, Cantidad in Datos['Bodegas'].items():
            print(f"Cantidad en Bodega {Bodega}: {Cantidad}")
        total = sum(Datos['Bodegas'].values())
        print(f"Cantidad Total: {total}")
    
    guardar = input("\n¿Desea guardar el reporte en un archivo de texto (sí/no)? ").lower()
    if guardar == 'sí':
        with open('reporte_inventario.txt', 'w') as file:
            for producto, Datos in inventario.items():
                file.write(f"\nProducto: {producto}\n")
                file.write(f"Nombre: {Datos['Nombre']}\n")
                file.write(f"Proveedor: {Datos['Proveedor']}\n")
                for Bodega, Cantidad in Datos['Bodegas'].items():
                    file.write(f"Cantidad en Bodega {Bodega}: {Cantidad}\n")
                total = sum(Datos['Bodegas'].values())
                file.write(f"Cantidad Total: {total}\n")
        print("Reporte guardado correctamente en 'reporte_inventario.txt'.")
