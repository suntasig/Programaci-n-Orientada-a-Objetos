# Clase Producto que define un producto con atributos básicos: ID, nombre, cantidad y precio.
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Inicializa un producto con los atributos: ID, nombre, cantidad y precio.
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

# Clase Inventario que gestiona una lista de productos.
class Inventario:
    def __init__(self):
        # Inicializa una lista vacía para almacenar productos.
        self.productos = []

    # Método para agregar un producto al inventario.
    def agregar_producto(self, producto):
        # Verifica si el ID del producto ya existe en la lista de productos.
        if producto.id not in [p.id for p in self.productos]:
            # Si no existe, agrega el producto a la lista.
            self.productos.append(producto)
        else:
            # Si el ID ya existe, imprime un mensaje de error.
            print("El ID del producto ya existe")

    # Método para eliminar un producto del inventario según su ID.
    def eliminar_producto(self, id):
        # Recorre la lista de productos buscando el producto con el ID especificado.
        for producto in self.productos:
            if producto.id == id:
                # Si lo encuentra, lo elimina de la lista.
                self.productos.remove(producto)
                return
        # Si no encuentra el producto, imprime un mensaje de error.
        print("Producto no encontrado")

    # Método para actualizar la cantidad y/o el precio de un producto existente.
    def actualizar_producto(self, id, cantidad=None, precio=None):
        # Recorre la lista de productos buscando el producto con el ID especificado.
        for producto in self.productos:
            if producto.id == id:
                # Si se proporciona una nueva cantidad, actualiza el atributo cantidad.
                if cantidad is not None:
                    producto.cantidad = cantidad
                # Si se proporciona un nuevo precio, actualiza el atributo precio.
                if precio is not None:
                    producto.precio = precio
                return
        # Si no encuentra el producto, imprime un mensaje de error.
        print("Producto no encontrado")

    # Método para buscar productos por su nombre.
    def buscar_producto(self, nombre):
        # Retorna una lista de productos que coinciden con el nombre (ignorando mayúsculas/minúsculas).
        return [producto for producto in self.productos if producto.nombre.lower() == nombre.lower()]

    # Método para mostrar todos los productos en el inventario.
    def mostrar_productos(self):
        # Recorre la lista de productos y muestra la información de cada uno.
        for producto in self.productos:
            print(f"ID: {producto.id}, Nombre: {producto.nombre},"
                  f" Cantidad: {producto.cantidad}, Precio: {producto.precio}")

# Función principal que gestiona el menú de opciones para interactuar con el inventario.
def main():
    # Crea una instancia de la clase Inventario.
    inventario = Inventario()

    # Bucle infinito que muestra el menú y espera la selección del usuario.
    while True:
        print("Menú:")
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
            id = int(input("Ingrese ID del producto: "))
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            # Crea una nueva instancia de Producto y la agrega al inventario.
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            # Eliminar un producto por ID.
            id = int(input("Ingrese ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == "3":
            # Actualizar un producto existente.
            id = int(input("Ingrese ID del producto a actualizar: "))
            cantidad = int(input("Ingrese nueva cantidad del producto: "))
            precio = float(input("Ingrese nuevo precio del producto: "))
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == "4":
            # Buscar un producto por nombre.
            nombre = input("Ingrese nombre del producto a buscar: ")
            productos = inventario.buscar_producto(nombre)
            # Muestra los productos encontrados.
            for producto in productos:
                print(f"ID: {producto.id}, Nombre: {producto.nombre},"
                      f" Cantidad: {producto.cantidad}, Precio: {producto.precio}")
        elif opcion == "5":
            # Mostrar todos los productos en el inventario.
            inventario.mostrar_productos()
        elif opcion == "6":
            # Salir del programa.
            break
        else:
            # Manejar opción inválida.
            print("Opción inválida")
            procucto = Producto(10, "pantalon", 50, 30)
            print(procucto.id, procucto.nombre, procucto.cantidad, procucto.precio)

# Este código solo se ejecuta si el script se ejecuta directamente (no importado como módulo).
if __name__ == "__main__":
    main()
