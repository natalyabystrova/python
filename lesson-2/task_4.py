DEFAULT_LIST = [57.8, 46.51, 97.38, 25.61, 22.3, 8.2, 11.6, 33.15, 9.3, 97.7]


def formatter(value):
    roubles = int(value)
    kop = 100 * (value - roubles)
    a = f'{roubles} руб {kop:02.0f} коп'
    return a


string = ',  '.join(list(map(formatter, DEFAULT_LIST)))
print(string)
print(list(map(formatter, DEFAULT_LIST)))
print(id(DEFAULT_LIST))
DEFAULT_LIST.sort()
print(list(map(formatter, DEFAULT_LIST)))
print(id(DEFAULT_LIST))
sorted_list_float_desc = sorted(DEFAULT_LIST, reverse=True)
sorted_list_desc = list(map(formatter, sorted_list_float_desc))
print(sorted_list_desc)
print(id(sorted_list_float_desc))
print('Пять самых дорогих товаров:')
top_5 = list(map(formatter, sorted_list_float_desc[0:5]))
for x in top_5:
    print(x)
print('Пять самых дорогих товаров:')
for y in sorted_list_float_desc[0:5]:
    print(y)
