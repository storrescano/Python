menor=int(input("Introduzca un número: "))
mayor=int(input("Introduzca un número mayor que %d: "% (menor)))
while mayor<=menor:
    mayor=int(input("%d no es mayor que %d. Vuelve a introducir un número: "%(mayor,menor)))
print ("Los números que has escrito son %d y %d" %(menor, mayor))
