# region Task1
def print_friends_count():
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print('У тебя', friends_count, 'друг')
    elif friends_count >= 2 and friends_count <= 4:
        print('У тебя', friends_count, 'друга')
    elif friends_count >= 5 and friends_count < 20:
        print('У тебя', friends_count, 'друзей')
    else:
        print('Ого, сколько у тебя друзей! Целых', friends_count)
for friends_count in range(21):
    print_friends_count()
# endregion

# region Task2
friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']
# присвойте переменной index целочисленное значение,
# чтобы из списка friends была выбрана Алина
index = 3
print('Привет, ' + friends[index])
# endregion

# region Task3
print("Привет, я Анфиса!")
friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']
count = len(friends) # допишите свой код сюда
print(f"У тебя {count} друзей")
# endregion

# region Task4
# Здесь ваш код
months = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
          "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
# Запросите у пользователя номер месяца
month = int(input("Введите номер месяца "))
# Выведите соответствующий месяц
print(months [month-1])
# endregion
# region Task5
# Здесь ваш код
colors = ("красный", "синий", "зелёный", "жёлтый", "чёрный", "белый")
# Запросите у пользователя цвет
color = input("Введите цвет ")
# Проверьте, есть ли он в кортеже
if color in colors:
    print("Цвет найден")
else:
    print("Цвет не найден")
# endregion

# region Task6
friends =  {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск'
}
print(friends ['Серёга'])
# endregion

# region Task7
friends =  {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск'
}
# Ваш код здесь
friends ['Серёга'] = 'Оренбург'
print('Серёга теперь живёт в славном городе ' + friends['Серёга'])
# endregion

# region Task8
friends =  {
    'Серёга': 'Оренбург',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}
# Здесь ваш код
towns = set(friends.values())
for i in towns:
    print(i)
# endregion

# region Task9
friends = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Айгуль': 'Казань',
    'Алёна': 'Белгород'
}
friends["Даниил"] = "Санкт-Петербург"
print(friends)
# Напечатайте словарь friends
# endregion

#region Task10 Написать функцию, которая принимает список чисел и возвращает их сумму.
def sum_numbers (numbers):
    summa = 0
    for number in numbers:
        summa += number
    return summa
# endregion

region Task11 Написать функцию, которая принимает строку и возвращает количество гласных в ней.
def count_vowels(text):
    count = 0
    for leter in text:
        if leter in 'EUIOAeuioa':
            count += 1
    return count
# endregion

#region Task12 Написать функцию, которая принимает два списка и возвращает их пересечение.
def intersection(a,b):
    c = [value for value in a if value in b]
    return c
# endregion

# region Task13 Создайте список городов, удалите один из них и добавьте два новых.
citys = ["Москва", "Омск", "Киров", "Вологда"]
print(citys)
citys.remove("Вологда")
print(citys)
citys.append("Курск")
citys.append("Сочи")
print(citys)
# endregion

# region Task14 Напишите программу, которая находит уникальные элементы двух множеств.
def unique(set1,set2):
    set3 = (set1 ^ set2)
    return set3
# endregion

# region Task15 Создайте словарь студентов с баллами, найдите студента с максимальным баллом.
students =  {
    'Серёга': '123',
    'Соня': '124',
    'Миша': '22',
    'Дима': '99',
    'Алина': '111',
    'Егор': '564',
    'Коля': '12'
}
for key, value in students.items():
    students[key] = int(value)
balls = students.values()
max_ball = max(balls)
for key in students:
    if students[key] == max_ball:
        best_student = key
print(f"Студент с максимальным баллом это", best_student)
# endregion
