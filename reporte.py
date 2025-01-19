import os

def Reporte(inventario):
    directorio = 'reportes'
    ruta_completa = os.path.abspath(directorio)  
    print(f"Intentando crear el directorio en: {ruta_completa}")
    
    if not os.path.exists(ruta_completa):
        print(f"Creando directorio: {ruta_completa}")
        try:
            os.makedirs(ruta_completa)  
            print(f"Directorio '{ruta_completa}' creado con éxito.")
        except Exception as e:
            print(f"Error al crear el directorio: {e}")
            return  
    print("\nReporte de inventario:")
    for producto, Datos in inventario.items():
        print(f"\nProducto: {producto}")
        print(f"Código: {Datos['Codigo']}")
        print(f"Proveedor: {Datos['Proveedor']}")
        for Bodega, Cantidad in Datos['Bodegas'].items():
            print(f"Cantidad en Bodega {Bodega}: {Cantidad}")
        total = sum(Datos['Bodegas'].values())
        print(f"Cantidad Total: {total}")
    guardar = input("\n¿Desea guardar el reporte en un archivo de texto (sí/no)? ").lower()
    if guardar == 'sí':
        try:
            archivo_ruta = os.path.join(ruta_completa, 'reporte_inventario.txt')
            with open(archivo_ruta, 'w') as file:
                print("Guardando el reporte en el archivo...")
                for producto, Datos in inventario.items():
                    file.write(f"\nProducto: {producto}\n")
                    file.write(f"Código: {Datos['Codigo']}\n")
                    file.write(f"Proveedor: {Datos['Proveedor']}\n")
                    for Bodega, Cantidad in Datos['Bodegas'].items():
                        file.write(f"Cantidad en Bodega {Bodega}: {Cantidad}\n")
                    total = sum(Datos['Bodegas'].values())
                    file.write(f"Cantidad Total: {total}\n")
            print(f"Reporte guardado correctamente en '{archivo_ruta}'.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")


