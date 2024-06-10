from abc import ABC, abstractmethod

# Definimos la clase abstracta base Personaje
class Personaje(ABC):
    def __init__(self, nombre, fuerza, defensa):
        # Inicializa los atributos del personaje
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa
        self.vida = 10  # Vida inicial común a todos los personajes

    # Método para imprimir los atributos del personaje
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    # Método para aumentar los atributos del personaje al subir de nivel
    def subir_nivel(self, fuerza, defensa):
        self.fuerza += fuerza
        self.defensa += defensa

    # Método abstracto para verificar si el personaje está vivo
    @abstractmethod
    def esta_vivo(self):
        pass

    # Método abstracto para manejar la muerte del personaje
    @abstractmethod
    def morir(self):
        pass

    # Método abstracto para calcular el daño infligido a un enemigo
    @abstractmethod
    def daño(self, enemigo):
        pass

    # Método para realizar un ataque a un enemigo
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

# Definimos la clase Guerrero que hereda de Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, defensa, espada):
        # Inicializa los atributos del Guerrero y su espada
        super().__init__(nombre, fuerza, defensa)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

# Definimos la clase Mago que hereda de Personaje
class Mago(Personaje):
    def __init__(self, nombre, fuerza, defensa, libro):
        # Inicializa los atributos del Mago y su libro de hechizos
        super().__init__(nombre, fuerza, defensa)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.libro * self.fuerza - enemigo.defensa

# Función para simular un combate entre dos personajes
def combate(jugador_1, jugador_2):
    turno = 0
    # Mientras ambos personajes estén vivos, se alternan los turnos de ataque
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        if jugador_2.esta_vivo():
            print(">>> Acción de ", jugador_2.nombre, ":", sep="")
            jugador_2.atacar(jugador_1)
        turno += 1
    # Se determina el ganador al final del combate
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

# Creación de personajes Guerrero y Mago
personaje_1 = Guerrero("Guts", 20, 4, 4)
personaje_2 = Mago("Vanessa", 5, 4, 3)

# Muestra los atributos iniciales de ambos personajes
personaje_1.atributos()
personaje_2.atributos()

# Inicia el combate entre los dos personajes
combate(personaje_1, personaje_2)