# zadanie 3
print('{} {}'.format('Przykład', 'jeden'))
print('{:>100}'.format('przykład 2'))
print('{:^100}'.format('Przykład 3'))
print('{:+d}'.format(420))

data = {'first': 'Przykład', 'last': 'piąty'}
print('{first} {last}'.format(**data))