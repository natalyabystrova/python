class OwnError(Exception):
    pass


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as exc:
        raise OwnError(exc)


try:
    print(division(5, 2))
except OwnError:
    pass

a = 5
b = 0
try:
    division(a, b)
except OwnError as exc:
    print(f'На ноль делить нельзя. Введите положительный делитель. Введенные числа:'
          f' {a} (делимое), {b} (делитель)')
