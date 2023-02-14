"""Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
 умножение (mul()), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение,
 уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно"""

class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.simbol = '&'

    def __str__(self):
        return str(f'Количество ячеек - {self.cell}')

    def __sub__(self, other):
        return Cell(abs(self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def make_order(self, count):
        x = self.cell
        while x > 0:
            for k in range(1,count+1):
                print(self.simbol, end ='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end = '')



a = Cell(5)
b = Cell(10)
c = Cell(3)
d = Cell(2)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(3)
b.make_order(3)