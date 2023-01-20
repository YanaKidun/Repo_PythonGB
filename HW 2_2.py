# Задание 2. Реализовать обмен значений соседних элементов
number_elements = int(input("Количество элементов списка "))
Userlist = []
num = 0
g = 0
while num < number_elements:
    Userlist.append(input("Значение списка "))
    num += 1
print(Userlist)

long = int(len(Userlist) / 2)
for listelements in range(long):
    Userlist[g], Userlist[g + 1] = Userlist[g + 1], Userlist[g]
    g += 2
print(Userlist)
