# задание 4 Найти самую большую цифру в числе
maxvalue = int(input("Введите число, что бы найти самую большую цифру в числе >>>"))
string = str(maxvalue)
ls = list(map(int, string))
mavval = max(ls)
print("Самая большая цифра в числе {}".format(mavval))

