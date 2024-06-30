"""
Este programa convierte una medida en metros a pies y pulgadas.
Utiliza diferentes tipos de datos y muestra el uso adecuado de variables y funciones.
"""

def metros_a_pies_y_pulgadas(metros):
    """
    Convierte una medida en metros a pies y pulgadas.

    para metros: Medida en metros (float)
    return: Una tupla con la medida en pies y la medida restante en pulgadas (int, float)
    """
    pies_por_metro = 3.28084
    pulgadas_por_pie = 12

    # Convertir metros a pies
    total_pies = metros * pies_por_metro

    # Separar la parte entera de pies y la parte fraccionaria en pulgadas
    pies = int(total_pies)
    pulgadas = (total_pies - pies) * pulgadas_por_pie

    return pies, pulgadas


def main():
    """
    Función principal que ejecuta el programa.
    """
    print("Conversor de Metros a Pies y Pulgadas")

    # Solicita al usuario que ingrese la medida en metros
    metros_str = input("Introduce la medida en metros: ")

    try:
        # Convierte la entrada del usuario a un número flotante
        metros = float(metros_str)

        if metros < 0:
            print("La medida debe ser un número positivo.")
            return

        # Realiza la conversión utilizando la función definida
        pies, pulgadas = metros_a_pies_y_pulgadas(metros)

        # Muestra el resultado al usuario
        print(f"{metros} metros son equivalentes a {pies} pies y {pulgadas:.2f} pulgadas.")

    except ValueError:
        print("Por favor, introduce un número válido.")


# Ejecuta la función principal si este archivo se ejecuta como script
if __name__ == "__main__":
    main()
