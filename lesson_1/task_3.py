number = 1
while number <= 150:
    if number % 10 == 1 and number != 11 and number % 100 != 11:
        print(number, "процент")
    elif number % 100 == 11 or number % 100 == 12 or number % 100 == 13 \
            or number % 100 == 14 or number % 10 == 0 \
            or number % 10 == 5 or number % 10 == 6 or number % 10 == 7 \
            or number % 10 == 8 or number % 10 == 9:
        print(number, "процентов")

    else:
        print(number, "процента")
    number = number + 1
