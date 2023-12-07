import math

path = 'day1/data.txt'
mass_file = open(path,'r')

cyfry_slownie = {
    'one':'1',
    'two':'2', 
    'three':'3', 
    'four':'4', 
    'five':'5', 
    'six':'6', 
    'seven':'7', 
    'eight':'8', 
    'nine':'9'
    }

def first_line(data):
    sum = 0
    for line in data:
        for key in cyfry_slownie.keys():
            if line.find(key) != -1:
                line = line.replace(key,cyfry_slownie[key])
        print("------")
        print(line)
        calib = ""
        for char in line.strip():
            if char.isdigit():
                calib += char
                print("fir=" + char)
                break
        for i in range(len(line.strip()) - 1, -1, -1):
            if line.strip()[i].isdigit():
                calib += line.strip()[i]
                print("ost=" + line.strip()[i])
                break
        sum += int(calib)
        print("------")
    return sum


if mass_file is not None:
    print(first_line(mass_file))
else:
    print("Data file is empty")

mass_file.close()