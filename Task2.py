import datetime
import time
# задание 2 Перевод секунд в часы, минуты и секунды
sec = int(input("Введите количество секунд >>>"))
ty_res = time.gmtime(sec)
res = time.strftime("%H:%M:%S", ty_res)
print(res)

