"""Escribe un programa que le pida al usuario si quiere calcular 
si un número es primo con for o con while, por tanto, habrán dos 
funciones que se caracterizan por hacer ese mismo cálculo de una 
manera (con for y sin breaks), o de otra (con while). Ambas funciones 
devolverá true (si es es primo) o false (si no es primo). 
El programa principal informará del resultado. Además, como mejora 
puedes calcular el tiempo que tarda en encontrar la solución de una manera u otra. 


Sergio Torres Cano
"""
import time
def f(a):
    c=0
    for i in range (1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
def w(b):
    primo=False
    d=2
    while b%d!=0 and primo==False:
        d+=1
        if d==b:
            primo=True
    return primo
primo=int(input("Introduzca un número: "))
pregunta=input("Quiere saber el número primo con un while o un for? (w/f): ")
start_time=time.time_ns()
if pregunta=="w" or pregunta=="W":
    print (f(primo))
elif pregunta=="f" or pregunta=="F":
    print (f(primo))
final_time=time.time_ns()-start_time
print (f"Ha tardado {final_time} nanosegundos")