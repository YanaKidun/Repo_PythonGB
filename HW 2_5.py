# Задание 5 Реализовать структуру «Рейтинг».
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
my_list_chek = my_list.copy()
value = int(input("Введите число "))
while True:
        for el in range(len(my_list)):
            if my_list[el] == value:
                my_list_chek.insert(el + 1, value)
                break

            elif my_list[0] < value:
                my_list_chek.insert(0, value)
                break

            elif my_list[len(my_list)-1] > value:
                my_list_chek.append(value)
                break
        break


if len(my_list_chek) == len(my_list):
    for indx in range(len(my_list_chek) - 1, -1, -1):
        if value <= my_list_chek[indx]:
            my_list_chek.insert(indx + 1, value)
            break

print(f"Заданный список - {my_list}")
print(f"Новый список c элементом, введенным пользователем, - {my_list_chek}")



