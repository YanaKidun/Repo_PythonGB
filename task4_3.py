""" Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень."""


"""Вариант 1"""
def my_func (x,y):
    b = abs(y)
    c = 1
    z = x
    while c < b:
        z = z * x
        c += 1
    return z

print(f'Result - {my_func(int(input("Number 1")), int(input("Number 2")))}')

"""Вариант 2"""
def my_func1 (x,y):
    m = abs(y)
    k = x ** m
    return k

print(f'Result - {my_func1(int(input("Number 1")), int(input("Number 2")))}')