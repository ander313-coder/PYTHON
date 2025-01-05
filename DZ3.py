#region Task1 Фильтрация четных чисел

import random
numbers=[]
for _ in range(10):
    i = random.randint(0, 100)
    if i%2==0:
        numbers.append(i)
print(numbers)

#endregion
#region Task2 Подсчет гласных

s = input("Введите строку: ")
count = 0
glas = set("aeiou")
for letter in s:
    if letter in glas:
        count += 1
print(f"Количество гласных равно:",count)

# endregion
# region Task3 Сумма чисел в списке

summa = 0
for i in range(3):
    i=int(input("Введите число: "))
    summa=summa+i
print("Сумма чисел= ",summa)

# endregion
# region Task4 Удаление дубликатов

numbers = input("Введите список чисел: ")
rezult = []
for i in numbers:
    if i not in rezult:
       rezult.append(i)
print(rezult)

# endregion
# region Task5 Таблица умножения

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1
    print()
    i += 1

# endregion
# region Task6 Проверка на палиндром

s = str(input("Введите строку: "))
a = s[::-1]
if s == a:
  print("Это палиндром")
else:
  print("Это не палиндром")

# endregion
# region Task7 Сортировка списка

import random
numbers = [random.randint(1, 100) for i in range(10)]
print("Исходный список: ", numbers)
sort_numbers = sorted(numbers)
print("Отсортированный список: ", sort_numbers)

# endregion
# region Task8 Подсчет элементов в словаре

spisok = [{'фрукт' : 'апельсин', 'количество' : 100}, {'фрукт' : 'мандарин', 'количество' : 200}, {'фрукт' : 'лимон', 'количество' : 300}, {'фрукт' : 'лимон', 'количество' : 500}, {'фрукт' : 'мандарин', 'количество' : 600}]
povtor_spisok = {}
for i in spisok:
    if i['фрукт'] not in povtor_spisok:
        povtor_spisok[i['фрукт']] = i['количество']
    else:
        povtor_spisok[i['фрукт']] += i['количество']
for fruit, kol in sorted(povtor_spisok.items(), key=lambda x: x):
    print(fruit, kol)

# endregion
# region Task9 Угадай число

w: int = 10
while True:
    q: int = int(input("Введите число "))
    if q>w:
        print("Загадонное число меньше")
    elif q<w:
        print("Загадонное число больше")
    else:
        print("Угадал")
        break

# endregion
# region Task10 Сумма чисел до N

number = int(input("Введите число: "))
sum = 0
for i in range(1, number+1):
    sum += i
print(sum)

# endregion