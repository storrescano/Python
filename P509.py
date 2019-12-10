anchura=int(input("Introduzca la anchura del dibujo: "))
altura=int(input("Introduzca la altura del dibujo: "))
for i in range (altura):
    for j in range (anchura):
        if i==0 or i==(altura-1):
            print ("*" ,end='')
        else:
            if j==0 or j==(altura):
                print ("*", end='')
            else:
                print (" ", end='')
    print ("");
