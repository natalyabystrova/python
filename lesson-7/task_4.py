import os
from os.path import join

for root, _, files in os.walk('./lesson-7/some_data_adv 2', topdown=False):
    res = []
    for file_name in files:
        _size = os.stat(join(root, file_name)).st_size
        res.append(_size)
    _max = max(res)
    _min = min(res)

    result = {}
    for k in range(1, len(str(_max)) + 1):
        result[10 ** k] = 0

    for r in res:
        _s = len(str(r))
        _l = 10 ** (_s - 1)
        _r = 10 ** _s
        if _l < r < _r:
            result[_r] += 1

    print(result)


