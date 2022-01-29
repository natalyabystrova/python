duration = 0
while duration >= 0:
    duration = int(input("Duration:"))
    days = duration // 86400
    left_after_days = duration % 86400
    hours = left_after_days // 3600
    left_after_hours = left_after_days % 3600
    minutes = left_after_hours // 60
    seconds = left_after_hours % 60
    if days == 0 and hours == 0 and minutes == 0:
        print(f'duration = {duration}: {seconds} cек')
    elif days == 0 and hours == 0:
        print(f'duration = {duration}: {minutes} мин {seconds} cек')
    elif days == 0:
        print(f'duration = {duration}: {hours} час {minutes} мин {seconds} cек')
    else:
        print(f'duration = {duration}: {days} дн {hours} час {minutes} мин {seconds} cек')
