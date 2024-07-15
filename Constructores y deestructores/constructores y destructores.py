class Computadora:
    def __init__(self, marca, modelo):
        """
        Constructor de la clase Computadora.
        Inicializa los atributos marca y modelo, y simula encender la computadora.

        Args:
            marca (str): La marca de la computadora.
            modelo (str): El modelo de la computadora.
        """
        self.marca = marca
        self.modelo = modelo
        self.encendida = False
        self.encender()
        print(f"Computadora {marca} {modelo} encendida.")

    def encender(self):
        """
        Simula encender la computadora.
        """
        self.encendida = True

    def apagar(self):
        """
        Simula apagar la computadora.
        """
        self.encendida = False
        print(f"Computadora {self.marca} {self.modelo} apagada.")

    def __del__(self):
        """
        Destructor de la clase Computadora.
        Apaga la computadora si aún está encendida.
        """
        if self.encendida:
            self.apagar()
        print(f"Objeto Computadora {self.marca} {self.modelo} eliminado.")


class HabitacionHotel:
    def __init__(self, numero, tipo):
        """
        Constructor de la clase HabitacionHotel.
        Inicializa los atributos numero y tipo, y simula ocupar la habitación.

        Args:
            numero (int): El número de la habitación.
            tipo (str): El tipo de la habitación (simple, doble, suite, etc.).
        """
        self.numero = numero
        self.tipo = tipo
        self.ocupada = False
        self.ocupar()
        print(f"Habitación {numero} ({tipo}) ocupada.")

    def ocupar(self):
        """
        Simula ocupar la habitación del hotel.
        """
        self.ocupada = True

    def desocupar(self):
        """
        Simula desocupar la habitación del hotel.
        """
        self.ocupada = False
        print(f"Habitación {self.numero} desocupada.")

    def __del__(self):
        """
        Destructor de la clase HabitacionHotel.
        Desocupa la habitación si aún está ocupada.
        """
        if self.ocupada:
            self.desocupar()
        print(f"Objeto HabitacionHotel {self.numero} eliminado.")


# Demostración del uso de las clases y sus constructores y destructores

print("=== Demostración de Computadora ===")
computadora = Computadora('Dell', 'XPS 15')
# Aquí se podrían realizar operaciones con la computadora.
del computadora  # Esto activará el destructor para apagar la computadora

print("\n=== Demostración de HabitacionHotel ===")
habitacion = HabitacionHotel(98, 'Suite')
# Aquí se podrían realizar operaciones con la habitación.
del habitacion  # Esto activará el destructor para desocupar la habitación
