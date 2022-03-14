class OwnError(Exception):
    pass
lst = []
while True:
    try:
        number = input("Введите число")
        if number.isdigit():
            lst.append(int(number))
            print(lst)
        elif number == "stop":
            print(f'Программа завершена. {lst}')
            break
        else:
            raise OwnError("Вы ввели не число")
    except OwnError:
        print("Вы ввели не число. Введите число.")
