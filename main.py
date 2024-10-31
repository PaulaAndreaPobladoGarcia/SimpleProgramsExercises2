# Solicita al usuario que ingrese un año y lo convierte a un entero
year = int(input("Enter a year: "))

# Verifica si el año es anterior a 1582
if year < 1582:
    # Reglas del calendario juliano
    # Comprueba si el año es divisible por 4
    if year % 4 == 0:
        # Si es divisible por 4, es un año bisiesto
        print(f"{year} is a leap year.")
    else:
        # Si no es divisible por 4, no es un año bisiesto
        print(f"{year} is not a leap year.")
else:
    # Si el año es 1582 o posterior, aplica las reglas del calendario gregoriano
    # Comprueba si el año es divisible por 4 y no por 100, o si es divisible por 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # Si se cumple la condición, es un año bisiesto
        print(f"{year} is a leap year.")
    else:
        # Si no se cumple la condición, no es un año bisiesto
        print(f"{year} is not a leap year.")
