print("Bienvenido la tienda verde".center(30,'-'))
Productos_disponibles = {
    "(1)": "Camisetas",
    "(2)": "Camisetas Retro",
    "(3)": "Gorras",
    "(4)": "Bufandas",
    "(5)": "Uniformes",
    "(6)": "Guallos",
    "(7)": "Guantes"
}
print("Seleccione un producto de la lista")
for codigo, producto in Productos_disponibles.items():
    print(f"{codigo} = {producto}")

while True:
    codigo_producto = input("Ingrese el numero de su producto: ")
    if codigo_producto in Productos_disponibles:
        nombre_producto = Productos_disponibles[codigo_producto]
        print (f"tu producto es: {nombre_producto}")
        break
    else:
        print("Codigo invalido, por favor seleccione un codigo de la lista.")
