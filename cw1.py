import random
# zadanie 1
tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
# zadanie 2
imie1= "Patryk"
nazwisko1 = "Trela"
litera_1 = imie1[1]
litera_2 = nazwisko1[2]

print("W tekście jest", tekst.count(litera_1) ,"liter a oraz", tekst.count(litera_2) ,"liter e")

imie2 = "Norbert"
nazwisko2 = "Szmigiero"
litera_1 = imie2[1]
litera_2 = nazwisko2[2]

print("W tekście jest", tekst.count(litera_1) ,"liter o oraz", tekst.count(litera_2) ,"liter z")

# zadanie 4

#print(dir("Lubie placki"))
help("Lubie placki".endswith('.'))

# zadanie 5

dane1 = imie1 + " " + nazwisko1
dane2 = imie2 + " " + nazwisko2
print(dane1[::-1])
print(dane2[::-1])
#=======#



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
wartosc1 = ("22","n@wp.pl","1998","pstrowskiego 12")
wartosc2 = ("23","nor@wp.pl","1997","wolnosci 11")
wartosc3 = ("24","norbe@wp.pl","1996","generalow 10")

slownik = {krotka1:wartosc1,krotka2:wartosc2,krotka3:wartosc3}

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


#zad13
slownik1 = {"Rekord1", "Rekord2", "Rekord3"}
slownik2 = {"Kolor1", "Kolor2", "Kolor3"}
slownik3 = {"Moc1", "Moc2", "Moc3"}
lista_slownikow = [slownik1,slownik2,slownik3]


print(" ")
print(lista_slownikow)
