"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(x, y):
    return x ** y

# Не заметила необходимости в применении формулы. Оператор ** работает корректно на отрицательных числах
# def my_func(x, y):
#    return 1 / (x ** abs(y))


print(my_func(3.8, -4))


def my_func_2(x, y):
    result = x
    for i in range(abs(y)-1):
        result *= x
    return 1 / result


print(my_func_2(3.8, -4))
