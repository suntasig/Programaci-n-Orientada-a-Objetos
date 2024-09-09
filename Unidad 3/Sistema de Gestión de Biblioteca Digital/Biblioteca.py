class libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.informacion =(autor, titulo)
    def __str__(self):
        return f'ISBN: {self.isbn}, Titulo: {self.titulo}, Autor: {self.autor}, Categoria: {self}'

class usuario:
    def __init__(self, nombre,id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.lista_usuarios = []

class bliblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.id_usuario = set() # conjuntos
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f'el libro {libro.titulo} ya existe')
        else:
            self.libros[libro.isbn] =libro
            self.id_usuario.add(libro.isbn)
            print(f'el libro {libro.titulo}fue añadido')

    def quitar_libro(self, libro):
        if libro.isbn in self.libros:
            #del self.libros[libro.isbn]
            self.id_usuario.remove(libro.isbn)
            print(f'el libro {libro.titulo}fue eliminado')
        else:
            print(f'el libro {libro.titulo} no existe')
    def agregar_usuario(self,usuario):
        if usuario.id_usuario in self.usuarios:
            print(f'el usuario {usuario.id_usuario} ya existe')
        else:
            self.id_usuario.add(usuario.id_usuario)
            print('usuario agregado')

    def dar_baja_usuario(self,id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            #self.usuarios.pop(id_usuario)
            #self.id_usuario.remove(id_usuario)
            print(f'el usuario {id_usuario} ya existe')
        else:
            print(f'el usuario {id_usuario} no existe')
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print(f'El usuario {id_usuario} no existe')
        elif isbn not in self.libros:
            print(f'El libro {isbn} no existe')
        else:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            print(f'al usuario: {id_usuario} fue prestarado en el libro {libro.titulo}')

    def buscar_libro(self, termino_busqueda):
        resultados = [libro for libro in self.libros.values() if
        termino_busqueda.lower() in libro.titulo.lower() or termino_busqueda.lower() in libro.autor.lower()]
        if resultados:
            print("Resultados de búsqueda:")
            for libros in resultados:
                print(libros.titulo, libros)


# Menú para interactuar con la Biblioteca
def menu():
    biblioteca = bliblioteca()  # Crear una instancia de la biblioteca

    while True:
        print("1. Agregar Libro")
        print("2. Quitar Libro")
        print("3. Registrar Usuario")
        print("4. Dar de Baja Usuario")
        print("5. Prestar Libro")
        print("6. Buscar Libro")
        print("7. Salir")

        opcion= input("Seleccione una opción: ")

        if opcion == '1':  # Agregar libro
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            nuevo_libro = libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(nuevo_libro)

        elif opcion == '2':  # Quitar libro
            isbn = input("Ingrese el ISBN del libro a quitar: ")
            if isbn in biblioteca.libros:
                libro_a_quitar = biblioteca.libros[isbn]
                biblioteca.quitar_libro(libro_a_quitar)
            else:
                print(f"No se encontró ningún libro con ISBN {isbn}")

        elif opcion == '3':  # Registrar usuario
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            nuevo_usuario = usuario(nombre, id_usuario)
            biblioteca.agregar_usuario(nuevo_usuario)

        elif opcion == '4':  # Dar de baja usuario
            id_usuario = input("Ingrese el ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == '5':  # Prestar libro
            id_usuario = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == '6':  # Buscar libro
            termino_busqueda = input("Ingrese el término de búsqueda (título o autor): ")
            biblioteca.buscar_libro(termino_busqueda)

        elif opcion == '7':  # Salir del menú
            print("Saliendo del sistema. ¡Gracias!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()