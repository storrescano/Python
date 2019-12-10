"""Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata. El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.
Valor mínimo: 0
Valor máximo: 100
Piensa un número entre 0 y 100 a ver si lo puedo adivinar.
Es 50 ?: mayor
Es 75 ?: menor
Es 62 ?: menor
Es 56 ?: mayor
Es 59 ?: igual
Gracias por jugar!!
Mejoras (opcionales):
    • que al principio el programa se asegure de que el valor máximo es superior al valor mínimo.
    • Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le decimos "mayor" y al decir "26" le decimos "menor", el programa debe decir que estamos haciendo trampas y debe dejar de jugar con nosotros.
Sergio Torres Cano
"""
import random
minimo=int(input("Valor mínimo: "))
maximo=int(input("Valor máximo: "))
while maximo<=minimo:
    maximo=int(input("Introduzca un número mayor al mínimo: "))
pista=''
numero=random.randint(minimo,maximo)
pista=input("Es %d?: " %(numero))
while pista!="igual" and pista!="trampa":
    if pista=="menor":
        if (numero+1>maximo) or (numero-1<minimo):
            pista="trampa"
            print ("Eres un tramposo.")
        maximo=numero-1
        numero=random.randint(minimo,maximo)
        pista=input("Es %d?: " %(numero))
    elif pista=="mayor":
        if (numero+1>maximo) or (numero-1<minimo):
            pista="trampa"
            print ("Eres un tramposo.")
        minimo=numero+1
        numero=random.randint(minimo,maximo)
        pista=input("Es %d?: " %(numero))
if pista=="igual":
    print ("Gracias por jugar!")
else:
    print ("No quiero jugar más contigo.")
            
