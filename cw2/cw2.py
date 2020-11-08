import file_manager
import numbers
import chuck_norris

# zadanie 1

def laczListy(lista1, lista2):
    tab = []
    dlugosc = len(lista1) + len(lista2)
    a = 0
    b = 0
    for i in range(dlugosc):
        if i % 2 == 0 and a < len(lista1):
            tab.append(lista1[a])
            a += 1
        elif b < len(lista2):
            tab.append(lista2[b])
            b += 1
    return tab

# print(laczListy([0,0,0], [2, 5, 6, 7]))

# zadanie 2

def slownik(data_text):
    return {
        "length": len(data_text),
        "letters": list(data_text),
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower()
    }

# print(slownik("Szmatydełko"))

# zadanie 3

def usunLitere(text, letter):
    text = text.replace(letter.lower(), '')
    text = text.replace(letter.upper(), '')
    return text

# print(usunLitere("Alibaba", "a"))

# zadanie 4

def przeliczTemperature(base, temperature_type):
    if not isinstance(base, numbers.Number):
        print("To nie jest liczba")
    elif temperature_type == "Fahrenheit":
        return str(32 + 1.8 * base) + " °F "
    elif temperature_type == "Rankine":
        return str((base + 273.15) * 1.8) + " °R"
    elif temperature_type == "Kelvin":
        return str(base + 273.15) + " K"
    else:
        print("Podaj poprawną jednostkę temperatury")

print(przeliczTemperature(25, "Kelvin"))

# zadanie 10




#zad5

class Calculator:

    def __init__(self,liczba1,liczba2):
        self.liczba1 = liczba1
        self.liczba2 = liczba2

    def add(self):
        print(self.liczba1+self.liczba2)

    def difference(self):
        print(self.liczba1 - self.liczba2)

    def multiply(self):
        print(self.liczba1 * self.liczba2)

    def divine(self):
        if(self.liczba1 == 0 or self.liczba2 == 0):
            print("Divine by 0")
        else:
            print(self.liczba1 / self.liczba2)
#zad6

class ScinceCalculator(Calculator):
    def powering(self):
        print(pow(self.liczba1,self.liczba2))

kal = ScinceCalculator(3,4)
kal.add()
kal.difference()
kal.divine()
kal.powering()
#zad7

def reverse(napis):
    napis = napis[::-1]
    return napis
print(reverse("Norbert"))

#zad8
#plik file_maganer.py

#zad9
plik1 = file_manager.FileManager("test")
plik1.update_file("testowy tekst"+"\n")
print(plik1.read_file())

#zad10
obiekt1 = chuck_norris.norris("patryk")
obiekt1.wypisz()



