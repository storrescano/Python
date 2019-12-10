numero=input("Introduzca un número: ")
lista=[]
while numero != 'Salir':
    lista+=[numero]
    numero=input ("Introduzca otro número: ")
print ("Los números que has escrito son: ", end='')
print (lista)
