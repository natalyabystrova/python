lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директорм аэлита']
for elements in lst:
    string = elements.split(' ')
    print(f"Привет, {string[-1].capitalize()}!")
