# Definimos la clase base Personaje
class Personaje:
    # Constructor para inicializar los atributos del personaje
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # Método para imprimir los atributos del personaje
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    # Método para aumentar los atributos del personaje al subir de nivel
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    # Método para verificar si el personaje está vivo
    def esta_vivo(self):
        return self.vida > 0

    # Método para indicar que el personaje ha muerto
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # Método para calcular el daño que el personaje inflige a un enemigo
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

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
    # Constructor que inicializa los atributos del Guerrero y su espada
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    # Método para cambiar el tipo de espada del Guerrero
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    # Método para imprimir los atributos del Guerrero, incluyendo la espada
    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    # Método para calcular el daño del Guerrero, que incluye el factor de la espada
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

# Definimos la clase Mago que hereda de Personaje
class Mago(Personaje):
    # Constructor que inicializa los atributos del Mago y su libro de hechizos
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    # Método para imprimir los atributos del Mago, incluyendo el libro de hechizos
    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

    # Método para calcular el daño del Mago, que incluye el factor del libro de hechizos
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

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
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

# Muestra los atributos iniciales de ambos personajes
personaje_1.atributos()
personaje_2.atributos()

# Inicia el combate entre los dos personajes
combate(personaje_1, personaje_2)