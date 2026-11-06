# СПИСКИ

name = "Viktor"

# print(len(name))
# print(name[0])
# print(name[5])
# print(name[-1])
# print(name[-2])
# print(name[len(name)-1])

# СРЕЗЫ В СТРОКАХ
# name = "spring"

print(name[1:3])
print(name[3:])
print(name[:3])
print(name[:])
# строка[старт:стоп:шаг]
print(name[2::])
print(name[::-1])
print(name[::-2])

# name[0] = "W"  - не работает, строка неизменяема
# print(name)
name = name[0]
# print(name)

# МЕТОДЫ СТРОК
# name = "konstanTin"
# print(name)
# print(name.lower()) # приводит строку к нижнему регистру
# print(name.upper())
# print(name.capitalize())
# print(name.find("Tin"))
# print(name.count('t'))
# print(name.replace('T', "Z"))

# name = '    konstanTin    '
# print(name)
# print(name.strip())

# ФУНКЦИИ СТРОК
# print(len(name))
# print(len(name.strip()))

# ЭКРАНИРОВАННЫЕ ПОСЛЕДОВАТЕЛЬНОСТИ
# print('Hello world')
# print('Hello\nworld')
# print('Hello\tworld')
# print('Hello \'world')
# print('Hello \\world')
# print('Hello \world')

# Задание 1
# Пользователь вводит имя
# Вывести:
# Привет, (имя)!
# Длина имени:
# Первая буква:
# Последняя буква:

# Задание 2
# Пользователь вводит предложение
# Программа:
# убирает лишние пробелы по краям
# переводит текст в нижний регистр
# считает количество букв "а"
# заменяет все пробелы на _

# Задание 3
# Пользователь вводит слово
# Вывести слово в обратном порядке

# Задание 4
# Пользователь вводит с клавиатуры строку, слово для
# поиска, слово для замены. Произведите в строке замену
# одного слова на другое. Полученную строку отобразите
# на экране.