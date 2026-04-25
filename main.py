from inventario import *
from inventario import valor_total
from inventario import eliminar_producto
from inventario import actualizar_cantidad
from inventario import listar_productos
from inventario import agregar_producto

def menu():
    while True:
        print("\nSISTEMA DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Actualizar cantidad")
        print("4. Eliminar producto")
        print("5. Calcular valor total")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(nombre, precio, cantidad)
            print("Producto agregado correctamente.")

        elif opcion == "2":
            listar_productos()

        elif opcion == "3":
            nombre = input("Producto a actualizar: ")
            nueva = int(input("Nueva cantidad: "))
            if actualizar_cantidad(nombre, nueva):
                print("Cantidad actualizada.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Producto a eliminar: ")
            if eliminar_producto(nombre):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            print("Valor total del inventario:", valor_total())

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

menu()