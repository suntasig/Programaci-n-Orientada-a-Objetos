import os


# Clase Producto que define un producto con atributos básicos: ID, nombre, cantidad y precio.
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Inicializa un producto con los atributos: ID, nombre, cantidad y precio.
        self.id = id
        self.nombre = nombre
        self.cantidad =(cantidad)
        self.precio = (precio)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.cantidad} {self.precio}"


# Clase Inventario que gestiona una lista de productos.
class Inventario:
    def __init__(self):
        # Inicializa un diccionario vacío para almacenar productos.
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            if not os.path.exists('Inventario.txt'):
                with open('Inventario.txt', 'w') as file:
                    file.write("ID,Nombre,Cantidad,Precio\n")
            else:
                with open('Inventario.txt', 'r') as file:
                    next(file)  # Saltar la cabecera
                    for linea in file:
                        id, nombre, cantidad, precio = linea.strip().split(',')
                        self.productos[id] = Producto(id, nombre, int(cantidad), float(precio))
        except FileNotFoundError:
            print("El archivo 'Inventario.txt' no existe.")

    def guardar_inventario(self):
        with open('Inventario.txt', 'w') as file:
            file.write("ID,Nombre,Cantidad,Precio\n")  # Cabecera
            for producto in self.productos.values():
                file.write(f'{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n')

    # Método para agregar un producto al inventario.
    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print(f"El producto con ID {producto.id} ya existe.")
        else:
            self.productos[producto.id] = producto
            self.guardar_inventario()
            print("Producto agregado exitosamente.")

    # Método para eliminar un producto del inventario según su ID.
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")

    # Método para actualizar la cantidad y/o el precio de un producto existente.
    def actualizar_producto(self, id, cantidad, precio):
        if id in self.productos:
            self.productos[id].cantidad = int(cantidad)
            self.productos[id].precio = float(precio)
            self.guardar_inventario()
            print("Producto actualizado exitosamente.")
        else:
            print("Producto no encontrado.")

    # Método para buscar productos por su nombre.
    def buscar_producto_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values()
                      if producto.nombre.lower() == nombre.lower()]
        return resultados

    # Método para mostrar todos los productos en el inventario.
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos.values():
                print(
                    f"ID: {producto.id}, Nombre: {producto.nombre}, "
                    f"Cantidad: {producto.cantidad}, Precio: {producto.precio}")


# Función principal que gestiona el menú de opciones para interactuar con el inventario.
def main():
    # Crea una instancia de la clase Inventario.
    inventario = Inventario()

    # Bucle infinito que muestra el menú y espera la selección del usuario.
    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar productos")
        print("6. Salir")

        # Solicita al usuario que ingrese una opción.
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            # Agregar un nuevo producto.
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            # Crea una nueva instancia de Producto y la agrega al inventario.
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            # Eliminar un producto por ID.
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            # Actualizar un producto existente.
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = int(input("Ingrese nueva cantidad de productos: "))
            precio = float(input("Ingrese nuevo precio del producto: "))
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == "4":
            # Buscar un producto por nombre.
            nombre = input("Ingrese nombre del producto a buscar: ")
            productos = inventario.buscar_producto_nombre(nombre)
            # Muestra los productos encontrados.
            if productos:
                for producto in productos:
                    print(
                        f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == "5":
            # Mostrar todos los productos en el inventario.
            inventario.mostrar_productos()
        elif opcion == "6":
            # Salir del programa.
            break
        else:
            # Manejar opción inválida.
            print("Opción inválida.")


if __name__ == "__main__":
    main()
