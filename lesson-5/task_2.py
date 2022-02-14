def iterator_with_yield(start, stop, step):
    rez = start
    while rez < stop:
        yield rez
        rez += step


def iterator_with_yield_squared(start, stop, step):
    rez = start
    while rez < stop and rez ** 2 < 200:
        yield rez
        rez += step




