# inventario.py

productos = []

def agregar_producto(nombre, precio, cantidad):
    """Agrega un nuevo producto al inventario."""
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            producto["cantidad"] += cantidad
            return True
    
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    return True

def listar_productos():
    """Lista todos los productos del inventario."""
    if not productos:
        print("El inventario está vacío.")
        return
    
    print("\n--- INVENTARIO ---")
    print(f"{'Nombre':<20} {'Precio':<10} {'Cantidad':<10}")
    print("-" * 40)
    for producto in productos:
        print(f"{producto['nombre']:<20} ${producto['precio']:<9.2f} {producto['cantidad']:<10}")

def actualizar_cantidad(nombre, nueva_cantidad):
    """Actualiza la cantidad de un producto."""
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            producto["cantidad"] = nueva_cantidad
            return True
    return False

def eliminar_producto(nombre):
    """Elimina un producto del inventario."""
    for i, producto in enumerate(productos):
        if producto["nombre"].lower() == nombre.lower():
            productos.pop(i)
            return True
    return False

def valor_total():
    """Calcula el valor total del inventario."""
    total = 0
    for producto in productos:
        total += producto["precio"] * producto["cantidad"]
    return total