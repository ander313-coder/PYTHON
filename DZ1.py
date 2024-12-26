#ДЗ_1 конвертация температур
t:float=int(input("введите температуру в цельсиях: "))
f:float=int(1.8*t+32)
print(f)
#ДЗ_2 перевод времени
time = int(input("Введите кол-во секунд: "))
m=60
h=60 * m
hours = time//h
time %= h
min = time//m
time %= m
s = time
print(f"{hours} часов, {min} минут, {s} секунд")
#ДЗ_3 мили в км
km = float(input("Введите кол-во километров: "))
m=km*0.621371
print(m)
#ДЗ_4 футы в метры
f = float(input("Введите кол-во футов: "))
m=f*0.3048
print(m)
#ДЗ_5 площадь треугольника
base  = int(input("Введите длину основания треугольника: "))
height = int(input("Введите высоту треугольника: "))
A=(base * height)/2
print("Площадь треугольника: ",A)