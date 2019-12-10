#Progrgama codificado por:
#David González Lastra
#Néstor Paez Martinez
#Sergio Torres Cano
#Adrián Arias Alonso
#Angel Losada Ramos


#Objetivo del juego:
#El objetivo de UNO es deshacerse de todas las cartas que se “roban” inicialmente
#diciendo la palabra “UNO” cuando queda la última carta en la mano.
# Se reciben puntos por todas las cartas que los otros
#jugadores todavía tienen en sus manos (véase puntos).

import random
import os

def carta_tirada(carta_puesta,Lista_jugadores):
    global turno
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range (len(Lista_jugadores[turno])):
        print (f"[{i+1}]  {Lista_jugadores[turno][i]}")
    print (f"La carta puesta es {carta_puesta}")
    carta_lanzada=int(input("¿Que carta quieres tirar? Si quieres robar, escribe 0: "))
    comprobacion1=Lista_jugadores[turno][carta_lanzada-1].split(" ")
    comprobacion2=carta_puesta.split(" ")
    if carta_lanzada==0:
        cambio=random.choice(mazo)
        Lista_jugadores[turno].append(cambio)
        mazo.remove(cambio)
        cambiarTurnoDerecha(Lista_jugadores,carta_puesta)
    elif comprobacion1[1]==comprobacion2[1] or comprobacion1[0]==comprobacion2[0]:
        carta_puesta=Lista_jugadores[turno][carta_lanzada-1]
        mazo.append(Lista_jugadores[turno][carta_lanzada-1])
        Lista_jugadores[turno].remove(carta_puesta)
        if len(Lista_jugadores[turno])==0:
            print ("Enhorabuena, has ganado.")
        else:
            cambiarTurnoDerecha(Lista_jugadores,carta_puesta)
    else:
        print ("No puedes tirar esta carta.")
        carta_tirada(carta_puesta,Lista_jugadores)
        

def menuinstrucciones():
    os.system('cls' if os.name == 'nt' else 'clear')
    print (reglas)

def definirjugadores(jugadores,mazo):
    global turno
    numjugadores=int(input("¿Cuantos jugadores vais a jugar? (Máximo 4, mínimo 2)\n"))
    Lista_jugadores=[]
    if numjugadores>1 and numjugadores<5:
        for i in range (numjugadores):
            jugador=[]
            Lista_jugadores+=[jugador]
            for j in range (7):
                agregado=random.choice(mazo)
                Lista_jugadores[i].append(agregado)
                mazo.remove(agregado)
        carta_puesta=random.choice(mazo)
        mazo.remove(carta_puesta)
    else:
        print ("El número de jugadores no es correcto, vueva a introducir un número.")
        definirjugadores(jugadores)
    turno=random.randint(0,len(Lista_jugadores)-1)
    carta_tirada(carta_puesta,Lista_jugadores)

def cambiarTurnoDerecha(Lista_jugadores,carta_puesta):
    global turno
    turno+=1
    if turno==len(Lista_jugadores):
        turno=0
    print (Lista_jugadores[turno])
    carta_tirada(carta_puesta,Lista_jugadores)

#=================================Programa principal=================================#

reglas=("""
================================================================================
                                    UNO
================================================================================
    - Tendra un minimo de 2 jugadores y un maximo de 4.
    - Gana el jugador que se quede sin cartas en la mano.
    - Si no puedes poner una carta, se robara del mazo hasta encontrar una que
    se pueda jugar.
    - Se reparten 7 cartas a cada jugador
    - Solo se puede poner una carta del mismo color o mismo número.
================================================================================
""")

mazo=["0 Azul","1 Azul","2 Azul","3 Azul","4 Azul","5 Azul","6 Azul","7 Azul",
"8 Azul","9 Azul","0 Verde","1 Verde","2 Verde","3 Verde","4 Verde","5 Verde",
"6 Verde","7 Verde","8 Verde","9 Verde","0 Amarillo","1 Amarillo","2 Amarillo",
"3 Amarillo","4 Amarillo","5 Amarillo","6 Amarillo","7 Amarillo","8 Amarillo",
"9 Amarillo","0 Rojo","1 Rojo","2 Rojo","3 Rojo","4 Rojo","5 Rojo","6 Rojo",
"7 Rojo","8 Rojo","9 Rojo",
"0 Azul","1 Azul","2 Azul","3 Azul","4 Azul","5 Azul","6 Azul","7 Azul",
"8 Azul","9 Azul","0 Verde","1 Verde","2 Verde","3 Verde","4 Verde","5 Verde",
"6 Verde","7 Verde","8 Verde","9 Verde","0 Amarillo","1 Amarillo","2 Amarillo",
"3 Amarillo","4 Amarillo","5 Amarillo","6 Amarillo","7 Amarillo","8 Amarillo",
"9 Amarillo","0 Rojo","1 Rojo","2 Rojo","3 Rojo","4 Rojo","5 Rojo","6 Rojo",
"7 Rojo","8 Rojo","9 Rojo"]


jugadores=[]

salir=False
turno=0
print(random.choice(mazo))
while salir==False:
    print ("=========================")
    print ("=     M   E   N   Ú     =")
    print ("=========================")
    print (" 1) Instrucciones ")
    print (" 2) Jugar ")
    print (" 3) Salir ")              
    print ("=========================") 
    indice=int(input("Elije una opción:"))
    if indice==1:
        menuinstrucciones()
    elif indice==2:
        definirjugadores(jugadores,mazo)
        salir=True
    elif indice==3:
        salir=True
    elif indice==4:
        print (mazo)
    else:
        print("Opción incorrecta, vuelva a intentarlo")


