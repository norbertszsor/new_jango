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



