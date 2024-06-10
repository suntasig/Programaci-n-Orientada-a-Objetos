class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        # Atributos privados
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    # Método  para mostrar atributos
    def atributos(self):
        print(self.__nombre, ":", sep="")
        print("·Fuerza:", self.__fuerza)
        print("·Inteligencia:", self.__inteligencia)
        print("·Defensa:", self.__defensa)
        print("·Vida:", self.__vida)

    # Métodos para acceder a los atributos
    def get_nombre(self):
        return self.__nombre

    def get_fuerza(self):
        return self.__fuerza

    def get_inteligencia(self):
        return self.__inteligencia

    def get_defensa(self):
        return self.__defensa

    def get_vida(self):
        return self.__vida

    # Métodos para modificar los atributos
    def set_vida(self, vida):
        self.__vida = vida

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa

    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")

    def daño(self, enemigo):
        return self.__fuerza - enemigo.get_defensa()

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.set_vida(enemigo.get_vida() - daño)
        print(self.get_nombre(), "ha realizado", daño, "puntos de daño a", enemigo.get_nombre())
        if enemigo.esta_vivo():
            print("Vida de", enemigo.get_nombre(), "es", enemigo.get_vida())
        else:
            enemigo.morir()


class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.__espada = espada

    # Método para cambiar el arma
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.__espada = 8
        elif opcion == 2:
            self.__espada = 10
        else:
            print("Número de arma incorrecta")

    # Sobrescribir método para mostrar atributos
    def atributos(self):
        super().atributos()
        print("·Espada:", self.__espada)

    # Sobrescribir método para calcular daño
    def daño(self, enemigo):
        return self.get_fuerza() * self.__espada - enemigo.get_defensa()


class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.__libro = libro

    # Sobrescribir método para mostrar atributos
    def atributos(self):
        super().atributos()
        print("·Libro:", self.__libro)

    # Sobrescribir método para calcular daño
    def daño(self, enemigo):
        return self.get_inteligencia() * self.__libro - enemigo.get_defensa()


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.get_nombre(), ":", sep="")
        jugador_1.atacar(jugador_2)
        if jugador_2.esta_vivo():
            print(">>> Acción de ", jugador_2.get_nombre(), ":", sep="")
            jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.get_nombre())
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.get_nombre())
    else:
        print("\nEmpate")


# Creación de personajes y ejecución del combate
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)
