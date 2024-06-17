 #Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Función para identificar los días de la semana con temperaturas superiores al promedio
def dias_calurosos(temperaturas, promedio):
    dias_calurosos = []
    for i in range(len(temperaturas)):
        if temperaturas[i] > promedio:
            dias_calurosos.append(i+1)
    return dias_calurosos

# Main
if __name__ == "__main__":
    # Ingresar temperaturas diarias
    temperaturas = ingresar_temperaturas()

    # Calcular promedio semanal
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio}")

    # Identificar días de la semana con temperaturas superiores al promedio
    dias_calor = dias_calurosos(temperaturas, promedio)
    if dias_calor:
        print("Los días con temperaturas superiores al promedio son: ")
        for dia in dias_calor:
            print(f"Día {dia}")
    else:
        print("No hubo días con temperaturas superiores al promedio.")