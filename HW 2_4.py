# Задание 4. Вывести каждое слово с новой строки

user_string = input("Введите строку")
work_string = user_string.split(" ")
number_word: int = 1
number_wl: int = 0
control_len = len(work_string)

while control_len > number_wl:
    if len(work_string[number_wl]) < 10:
        print("Номер слова - {} Слово -{}.".format(number_word, work_string[number_wl]))
        number_word = number_word + 1
        number_wl = number_wl + 1
    else:
        print("Номер слова - {} Слово -{}.".format(number_word, work_string[number_wl][0:10]))
        number_word = number_word + 1
        number_wl = number_wl + 1
