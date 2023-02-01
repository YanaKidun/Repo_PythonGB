"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

def summary():
    try:
        with open('HW_T_5', 'w+') as work_obj:
            line = input('Numbers \n')
            work_obj.writelines(line)
            str_numb = line.split()
            print(str_numb)
            print(sum(map(int, str_numb)))
    except IOError:
        print('Error')
    except ValueError:
        print('Error')
summary()