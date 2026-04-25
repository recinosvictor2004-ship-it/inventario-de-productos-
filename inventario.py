inventario = []

def agregar_producto(nombre, precio, cantidad):
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })

def listar_productos():
    if not inventario:
        print("\nNo hay productos registrados.\n")
        return

    print("\nInventario de productos\n")
    for i, p in enumerate(inventario, 1):
        print(f"{i}. {p['nombre']}")
        print(f"   Precio: {p['precio']}")
        print(f"   Cantidad: {p['cantidad']}")
    
def actualizar_cantidad(nombre, nueva_cantidad):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            p["cantidad"] = nueva_cantidad
            return True
    return False