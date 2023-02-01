"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. В программу должна попадать строка из
слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func()."""


"""Вариант 1 """
def int_func (arg):
    return print(arg.capitalize())

str1 = input("input str").split()
for items in str1:
    int_func(items)

"""Вариант 2 """
def int_func (arg):
    return (arg.capitalize())

str1 = input("input str").split()
str2 = list(str1)
new_list =[]
a = len(str2)
for items in str2:
    new_list.append(int_func(items))

print(new_list)




