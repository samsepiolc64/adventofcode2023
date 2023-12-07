import math

path = 'day1/data.txt'
mass_file = open(path,'r')

def first_line(data):
    for line in data:
        for char in line.strip():
            if char.isdigit():
                print ('p' + char, end=' ')
        for i in range(len(line.strip()) - 1, -1, -1):
            if line.strip()[i].isdigit():
                print ('o' + line.strip()[i])
                
        


if mass_file is not None:
    print("Temp data", first_line(mass_file))
else:
    print("Data file is empty")

mass_file.close()