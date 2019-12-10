a=input("¿Quiere hallar el area de un cuadrado o un triangulo?: ")
if a=="cuadrado" or a=="Cuadrado":
    b=float(input("Introduzca la longitud del lado del cuadrado: "))
    print ("El area del cuadrado es %.2f" %(b**2))
elif a=="triangulo" or a=="Triangulo":
    b=float(input("Introduzca la base del triangulo: "))
    h=float(input("Introduzca la altura del triangulo: "))
    print ("El area del triangulo es %.2f" %((b*h)/2))
else:
    print ("ERROR. No ha introducido lo que se le ha pedido. ")
