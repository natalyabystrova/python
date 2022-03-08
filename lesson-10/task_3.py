from math import floor
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат: {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __floordiv__(self, other):
        return Cell(floor(self.quantity // other.quantity))

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Cell(int(self.quantity - other.quantity))
        else:
            return f'Невозможно напечатать отрицательный результат'

    def make_order(self, quantity_in_row):
        row = ''
        for i in range(int(self.quantity / quantity_in_row)):
            row += f'{"*" * quantity_in_row} \n'
        row += f'{"*" * (self.quantity % quantity_in_row)}'
        return row

c1 = Cell(25)
c2 = Cell(20)
c3 = c1 - c2
с4 = Cell(50)
c5 = Cell(1)
c6 = Cell(3)
c7 = Cell(100)
print(c1.make_order(10))
print(c1 + c2)
print(c2 - c1)
print(c1 // c2)
print(c1 * c2)
print(c3.make_order(10))


