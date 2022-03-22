class OwnError(Exception):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def division(self):
        try:
            res = self.number1 / self.number2
        except ZeroDivisionError:
            print(f'На ноль делить нельзя. Введите положительный делитель. Введенные числа:'
                  f' {self.number1} (делимое), {self.number2} (делитель)')
        else:
            print(f'Программа выполняется корректно. Результат : {round(res, 2)}')
        finally:
            print("Программа завершена.")

c1 = OwnError(5, 2)
c2 = OwnError(5, 0)
c1.division()
c2.division()