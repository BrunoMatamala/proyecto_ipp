#Elige dos palabras del mismo largo en las que dos letras iguales no coincidan en la misma posición.
#cualquier "m" que aparezca en una frase será reemplazada por una "p", las letras "o" 
#se reemplazan por "e", "r" por "l", "e" por "i", "n" por "t" y "a" por "o".
#Crea un programa que:
#1. Permita al usuario elegir dos palabras que cumplan con las condiciones mencionadas anteriormente.
#2. Solicite al usuario que ingrese una frase.
#3. Reemplace las letras según la regla establecida a partir de las palabras elegidas.
#4. Imprima la nueva frase con las letras reemplazadas.

def cambiodepalabra():
    def validador_depalabra(palabra1, palabra2):
        if len(palabra1) != len(palabra2):
            return False
        for i in range(len(palabra1)): 
            if palabra1[i] == palabra2[i]:
                return False
        return True
    
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")
    if not validador_depalabra(palabra1, palabra2):
        print("Las palabras no son válidas")
        return
    
    letras = dict(zip(palabra1, palabra2))
    frase = input("Ingresa la frase a transformar: ")
    frase_cambiada = ''.join([letras.get(letra, letra) for letra in frase])
    print("La frase transformada es:", frase_cambiada)

cambiodepalabra()