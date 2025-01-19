from Cargar import Cargar_Inventario
from Guardar import Guardar_inventario
from registrar import Registrar_producto
from Ingresar import Ingresar_producto
from retiro import Retirar_producto
from buscar import Buscar_producto
from Historial import Historial_producto
from Reporte import Reporte

opcion = 0
Nombre = input("Ingrese su Nombre y apellido: ")
print("Hola ", Nombre)

def Mostrar_menu():
        print("\n MENU:")
        print("1: Registrar producto")
        print("2: Ingresar producto al inventario")
        print("3: Retirar producto del inventario")
        print("4: Buscar producto")
        print("5: Ver historial de producto")
        print("6: Reporte del inventario")
        print("7: Salir.")
def main():
        inventario = Cargar_Inventario()
        while True:
            Mostrar_menu()
            opcion = input ("Selecione una opcion: ")
            if opcion == "1":
                   Codigo = input ("Ingrese el codigo del producto:")
                   Nombre = input ("Ingrese el Nombre del producto:")
                   proveedor = input("Ingrese el proveedor del producto:")
                   Registrar_producto(inventario, Codigo, Nombre, proveedor)
            elif opcion == "2":
                   Nombre =  input("Ingrese el Nombre del producto:")
                   Cantidad = int(input("Ingrese la Cantidad del producto:"))
                   Bodega = input("Bodega (Norte, Centro Oriente):")
                   Ingresar_producto(inventario, Nombre, Cantidad, Bodega)
            elif opcion =="3":
                   Nombre = input("Ingrese el Nombre del producto:") 
                   Cantidad = int(input("Ingrese el monto a retirar:"))
                   Bodega = input ("Retirar de Bodega (Norte, Centro, Orinte):")
                   Descripcion = input ("Descripcion del retiro:")
                   Retirar_producto(inventario, Nombre, Cantidad, Bodega, Descripcion)
            elif opcion =="4":
                   Nombre = input("Ingrese el Nombre del producto:")
                   Buscar_producto(inventario, Nombre)
            elif opcion =="5":
                   Nombre = input("Ingrese el Nombre del producto:")
                   Historial_producto(inventario, Nombre)
            elif opcion == "6":
                Reporte(inventario)
            elif opcion == "7":
                Guardar_inventario(inventario)
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    main()
