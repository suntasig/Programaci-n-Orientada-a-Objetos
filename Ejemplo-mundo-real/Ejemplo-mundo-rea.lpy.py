# Directorio: EjemplosMundoReal_POO

# Archivo: sistema_reservas.py

# Definición de la clase Habitación
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Tipo de habitación (simple, doble, suite)
        self.precio = precio  # Precio por noche
        self.disponible = True  # Disponibilidad de la habitación

    def __str__(self):
        return f"Habitación {self.numero}: {self.tipo}, Precio por noche: ${self.precio}, Disponible: {self.disponible}"

    def reservar(self):
        """Marca la habitación como no disponible."""
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada exitosamente.")
        else:
            print(f"Habitación {self.numero} no está disponible.")

    def liberar(self):
        """Marca la habitación como disponible."""
        self.disponible = True
        print(f"Habitación {self.numero} liberada y ahora está disponible.")

# Definición de la clase Cliente
class Cliente:
    def __init__(self, nombre, dni):
        self.nombre = nombre  # Nombre del cliente
        self.dni = dni  # Documento de identidad del cliente
        self.reservas = []  # Lista de habitaciones reservadas

    def __str__(self):
        return f"Cliente: {self.nombre}, DNI: {self.dni}"

    def hacer_reserva(self, habitacion):
        """Realiza una reserva de una habitación."""
        if habitacion.disponible:
            habitacion.reservar()
            self.reservas.append(habitacion)
            print(f"{self.nombre} ha reservado la habitación {habitacion.numero}.")
        else:
            print(f"La habitación {habitacion.numero} no está disponible para reservar.")

    def cancelar_reserva(self, habitacion):
        """Cancela una reserva de una habitación."""
        if habitacion in self.reservas:
            habitacion.liberar()
            self.reservas.remove(habitacion)
            print(f"{self.nombre} ha cancelado la reserva de la habitación {habitacion.numero}.")
        else:
            print(f"{self.nombre} no tiene reservada la habitación {habitacion.numero}.")

# Definición de la clase Hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del hotel
        self.habitaciones = []  # Lista de habitaciones disponibles

    def __str__(self):
        return f"Hotel {self.nombre}"

    def agregar_habitacion(self, habitacion):
        """Agrega una nueva habitación al hotel."""
        self.habitaciones.append(habitacion)
        print(f"Habitación {habitacion.numero} agregada al hotel {self.nombre}.")

    def mostrar_habitaciones(self):
        """Muestra las habitaciones disponibles en el hotel."""
        print(f"Habitaciones en {self.nombre}:")
        for habitacion in self.habitaciones:
            print(habitacion)

# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear habitaciones
    h1 = Habitacion(101, "Simple", 50)
    h2 = Habitacion(102, "Doble", 80)
    h3 = Habitacion(201, "Suite", 150)

    # Crear hotel
    hotel = Hotel("Hotel Paraíso")
    hotel.agregar_habitacion(h1)
    hotel.agregar_habitacion(h2)
    hotel.agregar_habitacion(h3)

    # Mostrar habitaciones en el hotel
    hotel.mostrar_habitaciones()

    # Crear cliente
    cliente = Cliente("Ana Pérez", "12345678L")

    # Cliente hace reservas
    cliente.hacer_reserva(h1)
    cliente.hacer_reserva(h2)

    # Mostrar reservas del cliente
    for reserva in cliente.reservas:
        print(f"Reserva de {cliente.nombre}: Habitación {reserva.numero}")

    # Cliente cancela una reserva
    cliente.cancelar_reserva(h1)

    # Mostrar habitaciones actualizadas en el hotel
    hotel.mostrar_habitaciones()
