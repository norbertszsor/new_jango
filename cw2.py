import numbers

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

