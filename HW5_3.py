"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32"""

import statistics
with open('HW_T_3', 'r') as file_data:
    employees = {}
    keys = []
    salary = []

    for line in file_data:
        key, value = line.split()
        employees[key] = int(value)
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')

    for key in employees.keys():
        keys.append(key)
    c = 0
    while c < len(keys):
        salary.append(employees[(keys[c])])
        c = c + 1
    print(f'average salary is :{round(sum(salary)/len(salary), 2)}')

    file_data.close()

