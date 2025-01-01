def calculadora():
    print("Bienvenido a la calculadora básica")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        try:
            opcion = int(input("Elige una operación (1/2/3/4): "))
            if opcion not in [1, 2, 3, 4]:
                print("Por favor, elige una opción válida.")
                continue

            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == 1:
                resultado = num1 + num2
                operacion = "suma"
            elif opcion == 2:
                resultado = num1 - num2
                operacion = "resta"
            elif opcion == 3:
                resultado = num1 * num2
                operacion = "multiplicación"
            elif opcion == 4:
                if num2 == 0:
                    print("No se puede dividir entre cero. Intenta de nuevo.")
                    continue
                resultado = num1 / num2
                operacion = "división"

            print(f"El resultado de la {operacion} es: {resultado}")
        
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        otra = input("¿Quieres realizar otra operación? (s/n): ").lower()
        if otra != 's':
            print("Gracias por usar la calculadora. ¡Adiós!")
            break

if __name__ == "__main__":
    calculadora()

