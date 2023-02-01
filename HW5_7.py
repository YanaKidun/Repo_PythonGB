"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста."""

from json import dumps
new_file = []
with open('HW_T_7', 'r') as filehandle:
    test_str = filehandle.readlines()
    for line in test_str:
        a = line[:-1]
        new_file.append(a)
print(new_file)

SRC_FILENAME = new_file
DST_FILENAME = "HW_T_7json.json"

results = [{}, {}]


try:
    with open('HW_T_7') as fhs:
        lines = fhs.readlines()

    for line in lines:
        name, _, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)

    results[1]['average_profit'] = round(
        sum(
            profit for _, profit in results[0].items() if profit > 0
        ) / len(results[0])
    )

    with open(DST_FILENAME, "w") as fhd:
        fhd.write(dumps(results))
except IOError as e:
    print(e)
except ValueError:
    print("error")
    
#result json file:
# [{"firm_1": 5000, "firm_2": 4000, "firm_3": 42000, "firm_4": -5000, "firm_5": -3000}, {"average_profit": 10200}]


