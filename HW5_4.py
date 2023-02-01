"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""
# построчно записываем список
new_file = []

with open('HW_T_4', 'r') as filehandle:
    test_str = filehandle.readlines()
    for line in test_str:
        a = line[:-1]
        new_file.append(a)

# ищем и заменяем искомые слова в списке
a = 0
new_list = []
while a < len(new_file):
    str = new_file[a]
    k = str.find("-")
    b = str[0:k]
    if b == 'One':
        l = str.replace('One', 'Odin')
    elif b == 'Two':
        l = str.replace('Two', 'Dva')
    elif b == 'Three':
        l = str.replace('Three', 'Tri')
    elif b == 'Four':
        l = str.replace('Four', 'Cheture')
    new_list.append(l)
    a = a + 1

# построчно записываем отредактированные значения в новый список
file_name = input('Name: ')
f = open(file_name,'w')
for element in new_list:
    f.write(element)
    f.write('\n')

f.close()
filehandle.close()