import os
from os.path import join
from os import scandir
gen1 = scandir(join('./lesson-7/some_data_adv 2'))
result = {}
lst = []
lst_count = 0
lst_count2 = 0
for file in gen1:
    size = os.stat(file).st_size
    print(len(str(size)))
    lst.append(size)
print(lst)
for i in lst:
    if 10000 < i < 100000:
        lst_count += lst.count(i)
        result[100000] = lst_count
    elif 1000 <i < 10000:
        lst_count2 += lst.count(i)
        result[10000] = lst_count2

print(lst_count)
print(lst_count2)
print(result)

подпапки?

    # if result[k]:
    #     result[k] += 1
    # else:
    #     result[k] = 1
# lst = [1, 2, 3, 3]
# print(lst.count(3))