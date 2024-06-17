# Creamos una clase base para representar la información diaria del clima
class InformacionClima:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha
        self.temperatura = temperatura


# Creamos una clase que hereda de InformacionClima para representar la información diaria del clima con la humedad
class InformacionClimaHumedad(InformacionClima):
    def __init__(self, fecha, temperatura, humedad):
        super().__init__(fecha, temperatura)
        self.humedad = humedad


# Creamos una clase para calcular el promedio semanal de temperatura
class PromedioSemanal:
    def __init__(self):
        self.datos = []

    def agregar_dato(self, dato):
        self.datos.append(dato)

    def calcular_promedio_semanal(self):
        total_temperatura = 0
        for dato in self.datos:
            total_temperatura += dato.temperatura
        promedio_semanal = total_temperatura / len(self.datos)
        return promedio_semanal


# Ejemplo de uso
# Creamos objetos de la clase InformacionClimaHumedad
dato1 = InformacionClimaHumedad("2024-06-14", 25, 60)
dato2 = InformacionClimaHumedad("2024-06-15", 28, 55)
dato3 = InformacionClimaHumedad("2022-06-16", 27, 58)

# Creamos un objeto de la clase PromedioSemanal
promedio = PromedioSemanal()

# Agregamos los datos a nuestro objeto PromedioSemanal
promedio.agregar_dato(dato1)
promedio.agregar_dato(dato2)
promedio.agregar_dato(dato3)

# Calculamos el promedio semanal de temperatura
promedio_semanal = promedio.calcular_promedio_semanal()
print("El promedio semanal de temperatura es:", promedio_semanal)