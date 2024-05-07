#1. Confecciona un programa que solicite al usuario ingresar la temperatura en grados Celsius y la 
#convierta a grados Fahrenheit. Luego, se debe imprimir el resultado en pantalla.

#Debes crear un programa que dibuje una matriz, según las siguientes consideraciones:
#1. Solicitar la cantidad de filas.
#2. Solicitar la cantidad de columnas.
#3. Dibujar las filas y columnas solicitadas.


filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
for i in range(filas * 2 + 1):
    for j in range(columnas * 2 + 1):
        if i % 2 == 0 and j % 2 == 0: 
            print ("+", end="")
        elif i % 2 == 0:
            print("-", end="")
        elif j %  2 == 0:
            print("|", end="")     
        else:
            print(" ", end="")
    print()