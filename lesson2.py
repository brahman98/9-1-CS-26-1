# СТРОКИ И СПИСКИ. методы split() и join()
# a = 5
# b = 0

# students = ["Maxim", "Danil", "Viktor", "Alex", "Martin"]

# print(students[0])
# print(students[-1])
# print(students[len(students) - 1])

# data = ["Viktor", 27, 75, True]
# name = 0
# age = 1
# weight = 2
# check = 3

# print(f"Имя: {data[name]} \nВозраст: {data[age]} \nВес: {data[weight]} \nОнлайн: {data[check]}")

# СРЕЗЫ СПИСКОВ
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[1:3])
# print(numbers[:3])
# print(numbers[3:])
# print(numbers[::-1])
# print(numbers[старт:конец:шаг])

# МЕТОДЫ СПИСКОВ
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.append(20) # добавить элемент в конец списка
print(numbers)
numbers.insert(0, -1) # вставить значение по индексу (0 - индекс, -1 - значение)
print(numbers)
numbers.remove(1)
print(numbers)
numbers.pop(1)
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
# numbers.clear()
# print(numbers)

# ФУНКЦИИ ДЛЯ СПИСКОВ
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sum(numbers)/len(numbers))

print(0 in numbers)
print(10 in numbers)

# цикл + список
# for num in numbers:
#     print(num)

summa = 0
for num in numbers:
    # summa = summa + num
    summa += num
print(summa)

# ГЕНЕРАТОР СПИСКОВ
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)

numbers = [i for i in range(1, 6)]
print(numbers)

# [выражение for переменная in последовательность if условие]
numbers = [i for i in range(1, 11) if i % 2 == 0]
print(numbers)


# ЗАДАЧИ
# Задание 1 - оценки
# Создать список
# Программа должна вывести:
# -количество оценок
# -среднюю оценку
# -максимальную
# -минимальную

# Задание 2 - числа
# Создать список
# Вывести только четные числа

# Задание 3 - покупки
# Создать список с продуктами
# добавить 2 новых продукта
# удалить один продукт который был изначально
# вывести весь список через цикл for построчно

# Задание 4 - поиск
# Пользователь вводит число
# Сделать список.
# Программа должна определить, есть ли число в списке
# и сообщить об этом

# ДОМАШНЕЕ ЗАДАНИЕ
# Задание 1 - сколько раз встречается число в списке
# Вручную создать список, где есть число 
# которое повторяется несколько раз
# Вывести сообщение сколько раз встречается это число

# Задание 2 - мини-анализатор
# Создать список из 8-12 чисел
# Программа должна вывести
# Количество:
# Сумма:
# Минимум:
# Максимум:
# Четные числа:
# Нечетные числа: