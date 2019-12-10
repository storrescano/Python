"""Escribir un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y luego el usuario va probando valores. El programa va decidiendo si son demasiado grandes o pequeños. pista:
importe random
importe time
random.seed (time.time ())
minimo = int (input ( "Valor mínimo:"))
max = int (input ( "Valor máximo:"))
secreto = random.randint (mínimo, máximo)
Valor mínimo: 0
Valor máximo: 100
A ver si adivinas un número entero entre 0 y 100.
Escribe un número: 20
Demasiado pequeño! Volver a probar: 30
Demasiado grande! Volver a probar: 27
Correcto! Lo has intentado 3 veces.

Sergio Torres Cano
"""
import random
minimo=int(input("Valor mínimo: "))
maximo=int(input("Valor máximo: "))
secreto=random.randint(minimo,maximo)
i=1
numero=int(input("Escribe un número: "))
while i<3:
    if numero<secreto:
        numero=int(input("Demasiado pequeño! Volver a probar: "))
    elif numero>secreto:
        numero=int(input("Demasiado grande! Volver a probar: "))
    if numero==secreto:
        print ("Correcto! Lo has intentado %d veces." %(i))
        i=3
    elif i==2:
        print ("No es correcto! El número correcto era: %d"%(secreto))
    i+=1
