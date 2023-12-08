import os

path = 'day2/data.txt'
mass_file = open(path,'r')
datas = mass_file.read().splitlines()

colors = ['red', 'green', 'blue']

def packages(data):
        red = 0
        green = 0
        blue = 0
        game_count = 1
        czesci = data.split(":", 1)
        data = czesci[1].strip()
        tablice = data.split(';')
        tablice = [element.strip() for element in tablice]
        slowniki_kolorow = []
        for grupa in tablice:
            parts = grupa.split(', ')
            slownik_kolorow = {}
            for part in parts:
                ilosc, kolor = part.split()
                slownik_kolorow[kolor] = int(ilosc)
            slowniki_kolorow.append(slownik_kolorow)   
        return slowniki_kolorow

def key_sum(dane):
    suma_kolorow = {}

    for slownik in dane:
        for klucz, wartosc in slownik.items():
            suma_kolorow[klucz] = suma_kolorow.get(klucz, 0) + wartosc
    if suma_kolorow.get('red') == 12 and suma_kolorow.get('green') == 13 and suma_kolorow.get('blue') == 14:
         return true

def key_check(dane):
    coun = 0
    for pack in dane:
        if ((pack.get('red') is not None and pack.get('red') > 12) or (pack.get('green') is not None and pack.get('green') > 13) or (pack.get('blue') is not None and pack.get('blue') > 14)):
            coun += 1
    return coun

os.system('cls' if os.name == 'nt' else 'clear')
i = 1
sum = 0
for data in datas:
    print (key_check(packages(data)) )
    if key_check(packages(data)) < 1:
        sum += i
    i += 1
print(sum)

mass_file.close()