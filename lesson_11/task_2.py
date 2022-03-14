class OwnError(Exception):
    def __init__(self, number1):
        self.number1 = number1
        self.number2 = number2

number = int(input("Введите число"))
try:
    res = 100 / number
except ZeroDivisionError:
    print("На ноль делить нельзя. Введите положительное число.")
else:
    print(f'Программа выполняется корректно. Результат : {round(res, 2)}')
finally:
    print("Программа завершена.")