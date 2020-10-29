import numpy as np
import random

def losowe():
    randomlist = []
    for i in range(0,101):
        n = random.randint(100,200)
        randomlist.append(n)
    return randomlist


#zad6
lista = [i for i in range(1,11)]
lista2 = []

for i in range(1,11):
    if(i>5):
        lista.pop()
        lista2.append(i)

#zad7

lista3 = lista + lista2
lista3.insert(0,0)
lista4 = lista3.copy()
lista4.sort(reverse=True)
print(lista4)

#zad8
krotka1=(151101, "Rafał Szybło")
krotka2=(151102, "Parch Trela")
krotka3=(151103, "Ignatiew Ukarinko")
studenci = [krotka1,krotka2,krotka3]

#zad9

#zad10

numery = losowe()
print(numery)
numery2 = set(numery)
print(numery2)


#zad11
for i in range(1,10):
    print(numery[i], end=',')
print(' ')

#zad12
for i in range(100,20,-5):
    print(numery[i], end=',')



