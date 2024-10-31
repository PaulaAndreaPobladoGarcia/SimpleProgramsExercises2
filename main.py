# Función para realizar la división y mostrar resultados
def dividir(dividendo, divisor):
    cociente = dividendo // divisor  # División entera
    resto = dividendo % divisor  # Resto de la división

    # Verificar si la división es exacta
    if resto == 0:
        print("La división es exacta.")
    else:
        print("La división no es exacta.")

    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")

# Bucle para permitir múltiples divisiones
while True:
    # Pedir el dividendo
    dividendo = int(input("Introduce el dividendo: "))
    # Pedir el divisor y validar que no sea cero
    while True:
        divisor = int(input("Introduce el divisor (no puede ser cero): "))
        if divisor != 0:
            break
        print("Error: El divisor no puede ser cero.")

    # Llamar a la función para dividir
    dividir(dividendo, divisor)

    # Preguntar si se desea realizar otra operación
    continuar = input("¿Quieres hacer otra división? (s/n): ").lower()
    if continuar != 's':
        break