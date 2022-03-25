class OwnError(Exception):
    pass


def append(n):
    if n.isdigit():
        lst.append(int(number))
        print(lst)
        return True
    elif number == "stop":
        print(f'Программа завершена. {lst}')
        return False
    else:
        raise OwnError("Вы ввели не число")

lst = []
is_run = True
while is_run:
    try:
        number = input("Введите число")
        is_run = append(number)
    except OwnError:
        print("Вы ввели не число. Введите число.")
