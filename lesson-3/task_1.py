d1 = {
    'one': "один", 'two': "два", 'three': "три",
    'four': "четыре", 'five': "пять", 'six': "шесть",
    'seven': "семь", 'eight': "восемь", 'nine': "девять",
    'ten': "десять"
}

for key in d1:
    a = key.capitalize()


def num_translate(k):
    if k in d1.keys():
        print(d1[k])
        return d1[k]


num_translate('three')
