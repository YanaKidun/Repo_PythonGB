"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def task_3(a: float, b: float) -> float:

    try:
        return a / b
    except ZeroDivisionError as e:
        print('Нельзя делить на ноль')


division2_2 = lambda a, b: a / b if b else None

assert task_3(4, 2) == 2, 'division(4, 2) SOME TEXT'
assert task_3(14, 2) == 7, 'division(14, 2)'
assert task_3(0, 2) == 0, 'division(0, 2)'
assert task_3(-22, 4) == -5.5, 'division(-22, 4)'
assert task_3(1, 0) is None, 'division(1, 0)'
