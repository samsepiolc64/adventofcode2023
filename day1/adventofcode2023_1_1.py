import math

path = 'day1/data.txt'
mass_file = open(path,'r')

def first_line(data):
    sum = 0
    for line in data:
        calib = ""
        #print(line)
        for char in line.strip():
            if char.isdigit():
                # print ('p' + char, end=' ')
                calib += char
                break
        for i in range(len(line.strip()) - 1, -1, -1):
            if line.strip()[i].isdigit():
                #print ('o' + line.strip()[i])
                calib += line.strip()[i]
                break
        sum += int(calib)
    return sum
        
                
        


if mass_file is not None:
    print(first_line(mass_file))
else:
    print("Data file is empty")

mass_file.close()