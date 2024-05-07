
#Crea un programa en Python que solicite al usuario:
#1. Ingresar un número entero del 1 al 9.
#2. Que ingrese números secuenciales partiendo por 1, pero saltándose aquellos que sean múltiplos del valor ingresado al comienzo.
#3. En caso de ingresar un valor erróneo, enviar un mensaje indicando el error y el número que correspondía ingresar.

Numero_ingresado = int(input("Ingrese un número del 1 al 9: "))
if Numero_ingresado < 1 or Numero_ingresado > 9:
    print("El número debe estar entre el 1 y el 9")
else:
    contador = 1
    while True:
        entrada = int(input("Ingrese el siguiente número, evitando los múltiplos del número base : ".format(Numero_ingresado)))
        while contador % Numero_ingresado == 0:
            contador += 1 
        if entrada == contador:
            print("Número correcto")
        else:
            print("Error, el número correcto es ".format(contador))
            contador += 1