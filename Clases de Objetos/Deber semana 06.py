# Definición de una clase base
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad      # Atributo encapsulado
    def saludar(self):
        return f"Hola, me llamo {self._nombre} y tengo {self._edad} años."
    def obtener_edad(self):
        return self._edad
    def establecer_edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:
            print("La edad debe ser un número positivo.")
# Definición de una clase derivada
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self._salario = salario  # Atributo encapsulado
    def saludar(self):
        # Ejemplo de polimorfismo mediante sobrescritura de métodos
        return f"Hola, me llamo {self._nombre}, tengo {self._edad} años y gano {self._salario} dólares al año."
    def obtener_salario(self):
        return self._salario
    def establecer_salario(self, salario):
        if salario > 0:
            self._salario = salario
        else:
            print("El salario debe ser un número positivo.")
# Ejemplo de polimorfismo utilizando diferentes argumentos
def presentar_persona(persona):
    print(persona.saludar())
# Creación de instancias y demostración de funcionalidad
if __name__ == "__main__":
    # Creación de una instancia de Persona
    persona1 = Persona("Luis", 30)
    print(persona1.saludar())
    persona1.establecer_edad(34)
    print(f"Edad actualizada de {persona1._nombre}: {persona1.obtener_edad()} años")
    # Creación de una instancia de Empleado
    empleado1 = Empleado("KLeber", 25, 450)
    print(empleado1.saludar())
    empleado1.establecer_salario(500)
    print(f"Salario actualizado de {empleado1._nombre}: {empleado1.obtener_salario()} dólares")
    # Demostración de polimorfismo
    presentar_persona(persona1)
    presentar_persona(empleado1)
