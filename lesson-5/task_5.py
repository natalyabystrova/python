src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

"""убирает все повтряющиеся элементы:"""
_set = set()
tmp = set()
for x in src:
    if x not in tmp:
        _set.add(x)
    else:
        _set.discard(x)
    tmp.add(x)
unique_set = [x for x in src if x in _set]
print(unique_set)


""" с множествами (c сохранением одного элемента из повторяющихся):"""
def my_set(*args):
    _set = set()
    l = []
    for x in args:
        if x not in _set:
            _set.add(x)
            l.append(x)
    return l


print(my_set(*src))



# решение со списками:
new_lst = []
[new_lst.append(i) for i in src if i not in new_lst]
print(new_lst)


# с использованием словаря:
print(list(dict.fromkeys(src)))