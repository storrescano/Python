a=int(input("Introduce cuanto quiere sacar del cajero automático: "))
if a%500==0:
    print ("El cajero te devuelve %d billetes de 500 euros." %(a/500))
elif a%200==0:
    print ("El cajero te devuelve %d billetes de 200 euros." %(a/200))
elif a%100==0:
    print ("El cajero te devuelve %d billetes de 100 euros." %(a/100))
elif a%50==0:
    print ("El cajero te devuelve %d billetes de 50 euros." %(a/50))
elif a%20==0:
    print ("El cajero te devuelve %d billetes de 20 euros." %(a/20))
elif a%10==0:
    print ("El cajero te devuelve %d billetes de 10 euros." %(a/10))
elif a%5==0:
    print ("El cajero te devuelve %d billetes de 5 euros." %(a/5))
else:
    print("Introduzca un valor que sea divisor de 5")
