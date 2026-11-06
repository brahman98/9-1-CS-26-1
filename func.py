# ФУНКЦИИ В PYTHON

# def say_hello(name):
#     print("Hello!", name)

# name = "Maxim"
# say_hello("Viktor")
# say_hello(name)

# def show_sum(a, b):
#     return a + b

# print(show_sum(5, 10))
# summa = show_sum(5, 10)
# print(summa)

# Задание - написать 3 функции: 
# для деления/умножения, возведение в степень и остаток от деления

# def multiply(a, b):
#     return a * b
# print(multiply(3, 6))

# def power(a, b):
#     return a ** b
# print(power(3, 6))

# def lost(a, b):
#     return a % b
# print(lost(3, 6))

# def check_number(number):
#     if number > 0:
#         return "положительное число"
#     elif number < 0:
#         return "Отрицательное число"
#     else:
#         return "Ноль"

# print(check_number(10))
# print(check_number(-9))
# print(check_number(0))


def calculate_average(numbers):
    return sum(numbers) / len(numbers)

grades = [4, 2, 1, 5, 3, 4, 5]
average = calculate_average(grades)
print("Средняя оценка:", average)

# написать программу, которая добавляет в список только четные числа 
# (делаем доп переменную - пустой список, сразу после объявления функции)

def get_even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

nums = [5, 7, 2, 44, 78, 55]
print(get_even_numbers(nums))

# ПРАКТИКА
# ЗАДАНИЕ 1 - КАЛЬКУЛЯТОР ПЛОЩАДИ
# Создать функцию calc_area, которая принимает
# ширину и высоту прямоугольника и возвращает его площадь

# ЗАДАНИЕ 2 - Проверка возраста
# Создать функцию check_age(), которая возвращает строку:
# Доступ разрешен - если возраст 18  больше
# Доступ запрещен - в остальных случаях

# ЗАДАНИЕ 3 - Анализ списка
# Создать функцию analyze_nums(numbers), которая принимает
# список чисел и возвращает сумму, минимальное и максимальное значение

# ЗАДАНИЕ 4 - Калькулятор
# Создать функцию калькулятор с выбором операции:
# умножение/деление/сложение/вычитание/остаток от деления/степень
# Функция возвращает результат с информацией об операции


# МИНИ БАНК
def show_balance(balance):
    print("Ваш баланс:", balance, "руб")

def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print("Счет пополнен на", amount, "руб")
    else:
        print("сумма пополнения должна быть больше нуля")
    return balance

def withdraw(balance, amount):
    if amount <= 0:
        print("Сумма снятия должна быть больше нуля")
    elif amount > balance:
        print("Недостаточно средств")
    else:
        balance -= amount
        print("Вы сняли", amount, "руб")
    return balance

def main():
    balance = 1000
    while True:
        print("МИНИ-БАНКОМАТ")
        print("1 - Посмотерть баланс")
        print("2 - Пополнить баланс")
        print("3 - Снять деньги")
        print("4 - Выйти")

        choice = input("Выберите действие по цифре")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            amount == float(input("Сумма пополнения: "))
            balance = deposit(balance, amount)
        elif choice == "3":
            amount = float(input("Сумма снятия: "))
            balance = withdraw(balance, amount)
        elif choice == "4":
            print("До свидания")
            break
        else:
            print("Неверный пункт мнгю, попробуйте снова.")

main()