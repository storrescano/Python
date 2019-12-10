a=int(input("Introduzca el primer número: "))
b=int(input("Introduzca el segundo número: "))
c=int(input("Introduzca el tercer número: "))
d=int(input("Introduzca el cuarto número: "))
if a%d==0 and b%d==0 and c%d==0:
    print ("El cuarto número es divisor de los tres primeros números.")
else:
    print ("No es divisor de esos números.")
