""" Создать программно файл в текстовом формате, записать в него построчно данные,
пользователем. Об окончании ввода данных свидетельствует пустая строка."""

file_name = input('Name: ')
f = open(file_name,'w')
while True:
    s = input('Your text')
    if s == '':
        break
    f.write(s+'\n')
f.close()