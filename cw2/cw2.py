import file_manager


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



