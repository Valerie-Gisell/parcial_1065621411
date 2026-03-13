# Inventario simple

inventario = {}

# ---------- FUNCIONES ----------

def agregar_producto():
    nombre = input("Nombre del producto: ").lower()

    if nombre in inventario:
        print("El producto ya existe.")
        return

    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))

        if cantidad < 0 or precio < 0:
            print("Cantidad y precio deben ser positivos.")
            return

        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        print("Producto agregado.")

    except:
        print("Entrada inválida.")


def ver_inventario():
    if not inventario:
        print("Inventario vacío.")
        return

    total = 0

    print("\nInventario:")
    for nombre, datos in inventario.items():
        subtotal = datos["cantidad"] * datos["precio"]
        total += subtotal
        print(f"{nombre} | Cantidad: {datos['cantidad']} | Precio: {datos['precio']} | Total: {subtotal}")

    print("Valor total del inventario:", total)


def buscar_producto():
    nombre = input("Nombre del producto a buscar: ").lower()

    if nombre in inventario:
        datos = inventario[nombre]
        print(f"{nombre} | Cantidad: {datos['cantidad']} | Precio: {datos['precio']}")
    else:
        print("Producto no encontrado.")


def actualizar_cantidad():
    nombre = input("Producto a actualizar: ").lower()

    if nombre in inventario:
        try:
            nueva = int(input("Nueva cantidad: "))

            if nueva < 0:
                print("La cantidad debe ser positiva.")
                return

            inventario[nombre]["cantidad"] = nueva
            print("Cantidad actualizada.")

        except:
            print("Entrada inválida.")
    else:
        print("Producto no existe.")


def eliminar_producto():
    nombre = input("Producto a eliminar: ").lower()

    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")


# ---------- MENÚ ----------

while True:
    print("\n--- MENÚ INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Buscar producto")
    print("4. Actualizar cantidad")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_inventario()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        actualizar_cantidad()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")