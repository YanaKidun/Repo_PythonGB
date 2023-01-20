# Задание 1. Реализовать скрипт проверки типа данных каждого элемента
list1 = [20, 30, 40, "ii", "zzz", 9, 8]
print(list1)
number = len(list1)
print(number)
c = 0
while number > c:
    selection_value = list1[c]
    print(type(selection_value))
    c = c + 1
