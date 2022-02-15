def iterator_without_yield(n):
    gen1 = (el for el in range(1, n + 1, 2))
    return gen1

# для чисел, квадрат которых < 200:

def iterator_without_yield_squared(n):
    gen1 = (el for el in range(1, n + 1, 2) if el ** 2 < 200)
    return gen1

