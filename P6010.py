"""Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos. Nota: La lista en la que se guardan los nombres y notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]
Dame un nombre: Héctor Quiroga
Escribe una nota: 4
Escribe otra nota: 8.5
Escribe otra nota: 12
Dame otro nombre: Inés Valls
Escribe una nota: 7.5
Escribe otra nota: 1
Escribe otra nota: 2
Escribe otra nota: -5
Dame otro nombre:
Las notas de los alumnos son:
Héctor Quiroga: 4.0 - 8.5
Inés Valls: 7.5 - 1.0 - 2.0

Sergio Torres Cano
"""
lista=[]
nombre=input("Dame un nombre: ")
nota=float(input("Escribe una nota: "))
dentro=[nombre]
while nombre!='':
    if nota<=10 and nota>=0:
        dentro+=[nota]
        nota=int(input("Escribe una nota (Si no desea poner más,\
                        introduzca un número que no sea entre 0 y 10): "))
    else:
        lista+=[dentro]
        nombre=input("Dame un nombre (Si desea terminar, pulse enter): ")
        if nombre!='':
            dentro=[nombre]
            nota=float(input("Escribe una nota: "))
            if nota<=10 and nota>=0:
                dentro+=[nota]
                nota=float(input("Escribe una nota (Si no desea poner más,\
                                introduzca un número que no sea entre 0 y 10): "))
for i in range (len(lista)):
    for j in range (len(lista[i])):
        if j==0:
            print (lista[i][j], end=': ')
        elif j==(len(lista[i])-1):
            print (lista[i][j])
        else:
            print (lista[i][j], end=' - ')
