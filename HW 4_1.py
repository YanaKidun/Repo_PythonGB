"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В
 расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""


import sys
from lesson04 import my_mood


print(sys.argv)



try:
    time1, price1 = sys.argv
except ValueError:
    print("Invalid args")
    exit()

print(my_mood.user_salary(int(time1), int(price1)))