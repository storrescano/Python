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

def carta_tirada(carta_puesta,Lista_jugadores,lista_especiales):
    for i in range (len(Lista_jugadores[turno])):
        print (f"{i+1}.{Lista_jugadores[turno][i]}")
    print (carta_puesta)
    carta_lanzada=int(input("¿Que carta quieres tirar? Si quieres robar, escribe 0: "))
    if carta_lanzada==0:
        cambio=random.choice(mazo)
        Lista_jugadores[turno].append(cambio)
        mazo.remove(cambio)
        cambiarTurnoDerecha(Lista_jugadores,carta_puesta)
    elif len(Lista_jugadores[turno][carta_lanzada-1])==2:
        comprobacion2=list(Lista_jugadores[turno][carta_lanzada-1])
        print (comprobacion2)
        comprobante2=list(carta_puesta)
        print (comprobante2)
        if (comprobante2[1]==comprobacion2[1]) or (comprobante2[0]==comprobacion2[0]):
            print("Puedes tirar esta carta")
            carta_puesta=Lista_jugadores[turno][carta_lanzada-1]
            mazo.append(carta_puesta)
            Lista_jugadores[turno].remove(Lista_jugadores[turno][carta_lanzada-1])
            print (Lista_jugadores[turno])
            if len(Lista_jugadores[turno])==0:
                print ("Has ganado.")
            elif carta_lanzada in lista_especiales:
                especiales()
            else:
                cambiarTurnoDerecha(Lista_jugadores,carta_puesta)
        else:
            print ("No puedes tirar esta carta")
            carta_tirada(carta_puesta,Lista_jugadores,lista_especiales)
    else:
        comprobante=carta_puesta.split()
        print (comprobante)
        comprobacion=(Lista_jugadores[turno][carta_lanzada-1]).split()
        print (comprobacion)
        if (comprobante[1]==comprobacion[1]) or (comprobante[0]==comprobacion[0]):
            print("Puedes tirar esta carta")
            Lista_jugadores[turno].remove(carta_lanzada)
            carta_puesta=carta_lanzada
            if carta_lanzada in lista_especiales:
                especiales()
            else:
                cambiarTurnoDerecha(Lista_jugadores,carta_puesta)


def menuinstrucciones():
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
    carta_tirada(carta_puesta,Lista_jugadores,lista_especiales)

def cambiarTurnoDerecha(Lista_jugadores,carta_puesta):
    global turno
    if turno==0:
        turno+=1
        print (Lista_jugadores[0])
    elif turno==1:
        turno+=1
        print (Lista_jugadores[1])
        if len (Lista_jugadores)==2:
            turno=0
    if len(Lista_jugadores)==3:
        if turno==2:
            turno=0
            print (Lista_jugadores[2])
    elif len(Lista_jugadores)==4:
        if turno==2:
            turno+=1
            print (Lista_jugadores[2])
        elif turno==3:
            turno=0
            print (Lista_jugadores[3])
    carta_tirada(carta_puesta,Lista_jugadores,lista_especiales)

def cambiarTurnoIzquierda(Lista_jugadores,carta_puesta):
    if Lista_jugadores[turno]==0:
        turno=len(Lista_jugadores)
        print (Lista_jugadores[0])
    elif Lista_jugadores[turno]==1:
        turno-=1
        print (Lista_jugadores[1])
    elif Lista_jugadores[turno]==2:
        turno-=1
        print (Lista_jugadores[2])
    elif Lista_jugadores[turno]==3:
        turno-=1
        print (Lista_jugadores[3])
    carta_tirada(carta_puesta,Lista_jugadores,lista_especiales)

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
    - Solo se puede poner una carta del mismo color o mismo número, salvo las
    cartas especiales que se podran jugar independientemente del color que hay
    en la mesa.
================================================================================
""")

mazo=["0A","1A","2A","3A","4A","5A","6A","7A","8A","9A","0V","1V","2V","3V",
"4V","5V","6V","7V","8V","9V","0AM","1AM","2AM","3AM","4AM","5AM","6AM",
"7AM","8AM","9AM","0R","1R","2R","3R","4R","5R","6R","7R","8R","9R","+2A",
"+2R","+2V","+2AM","cambio_verde","cambio_azul","cambio_rojo",
"cambio_amarillo","prohibido_rojo","prohibido_azul","prohibido_verde",
"prohibido_amarillo","cambio_color","+4","0A","1A","2A","3A","4A","5A","6A",
"7A","8A","9A","0V","1V","2V","3V",
"4V","5V","6V","7V","8V","9V","0AM","1AM","2AM","3AM","4AM","5AM","6AM",
"7AM","8AM","9AM","0R","1R","2R","3R","4R","5R","6R","7R","8R","9R","+2A",
"+2R","+2V","+2AM","cambio_verde","cambio_azul","cambio_rojo",
"cambio_amarillo","prohibido_rojo","prohibido_azul","prohibido_verde",
"prohibido_amarillo","cambio_color","+4"]

lista_especiales=["cambio_verde","cambio_azul","cambio_rojo",
"cambio_amarillo","prohibido_rojo","prohibido_azul","prohibido_verde",
"prohibido_amarillo","cambio_color""+2A","+2R","+2V","+2AM","+4"]
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
    else:
        print("Opción incorrecta, vuelva a intentarlo")


