"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""
new_file = []
discipline_list = []
sum_dicspl = []
break_srt = []

with open('HW_T_6', 'r') as filehandle:
    test_str = filehandle.readlines()
    for line in test_str:
        a = line[:-1]
        new_file.append(a)
print(new_file)

# Отделяю название предметов от данных и записываю в 2 списка
a = 0
while a < len(new_file):
    str = new_file[a]
    k = str.find(":")
    b = str[0:k]
    c = str[k:]
    discipline_list.append(b)
    break_srt.append(c)
    a = a + 1

# подсчитываю сумму по часам по предмету, отбирая только цифры
n = 0
while n < len(break_srt):
    s = break_srt[n]
    l = len(s)
    integ = []
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))
            summary1 = sum(integ)
    n = n+1
    sum_dicspl.append(summary1)

# склеиваею 2 списка с названием дисциплин и суммарным количеством часов

result_dict = dict(zip(discipline_list, sum_dicspl))
print(result_dict)
# при таком варианте - в txt файл можно бесконечно много вносить дисциплин и часов.