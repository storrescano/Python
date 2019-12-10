palabra=input("Introduzca una palabra: ")
lista=[palabra]
puede=input("¿Desea introducir otra palabra? s/n: ")
while puede!='s' and puede!='n':
    puede=input("No lo ha escrito correctamente, ¿desea introducir otra? s/n: ")
while puede == 's':
    palabra=input("Introduzca otra palabra: ")
    lista+=[palabra]
    puede=input("¿Desea introducir otra palabra? S/N: ")
print ("Las palabras que has escrito son: ", end='')
print (lista)
