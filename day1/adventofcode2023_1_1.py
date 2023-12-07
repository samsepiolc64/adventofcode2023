import math

path = 'data.txt'
mass_file = open(path,'r')
data = mass_file.read().splitlines()

i = 1
suma = 0
ss=[12]


def pierwszy_wiersz(tekst):
    wiersze = tekst.split('\n')
    if wiersze:
        return wiersze[0]
    return None

# def sumator(data):
#     ss = []
#     for i in data:
#         s = math.floor(int(i)/3)-2
#         if s <= 0:
#             s = 0
#         ss.append(s)
#     return ss


# while sum(ss) != 0:
#     ss = sumator(data)
#     suma += sum(ss)
#     print('---')
#     print(ss)
#     print(suma)
#     data = ss


if data is not None:
    print("Pierwszy wiersz:", data)
else:
    print("Brak wierszy w tekście.")


mass_file.close()