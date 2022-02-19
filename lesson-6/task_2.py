import json
result = {}
fio = []
with open('./fio.csv', 'rt', encoding='utf-8') as f1:
    for line in f1:
        summa = ''
        lst = line.split(',')
        for elem in lst:
            summa += elem[0]
        fio.append(summa)

hobby = []
f2 = open('./hobby.csv', 'rt', encoding='utf-8')
for line in f2:
    line = line.replace("\n", "").replace(",", ";")
    hobby.append(line)
for i in range(0, len(fio)):
    _fio = fio[i]
    _hobby = hobby[i] if len(hobby) - 1 >= i else None
    result[_fio] = _hobby
print(result)

my_file = open(file="file1.json", mode='wt', encoding='utf-8' )
json.dump(result, my_file, indent=2, ensure_ascii=False)
my_file.close()
f2.close()
if len(hobby) > len(fio):
    exit(1)



# result = dict(zip(fio, hobby))
# print(result)

