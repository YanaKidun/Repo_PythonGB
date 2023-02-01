"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

try:
    with open("HW_T_2") as my_file:
        print(my_file.read())
except IOError:
    print("Some error")

try:
    with open('HW_T_2') as my_file:
        lines = 0
        words = 0
        symbols = 0
        for line in my_file:
            lines += 1
            words += len(line.split())
            symbols += len(line.strip('\n'))
        print("Lines:", lines)
        print("Words:", words)
        print("Symbols:", symbols)
except IOError:
    print('Some error')

my_file.close()