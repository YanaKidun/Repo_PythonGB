import datetime
import time

# задание 1 Ввод, вывод данных
a = 12
b = 10
print(a)
print(b)
value1 = int(input("Введите число >>>"))
print(value1)
username = input("Введите Ваше имя >>>")
useryear = int(input("Введите год Вашего рождения >>>"))
now = datetime.datetime.now()
nowyear = now.year
userage = nowyear - useryear
print("Привет, {}! Тебе уже {} лет! и число, которое Вы ввели {}".format(username, userage, value1))

