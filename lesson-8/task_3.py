def type_logger(func):
    def new_func(*args, **kwargs):
        params_txt = ', '.join(list(map(lambda a: f'{a}: {type(a)}', args)))
        params_txt += ', '.join(list(map(lambda k: f'{k}: {type(k)}', kwargs)))
        print(f'Call for: {func.__name__}')
        print(params_txt)
        res = func(*args, **kwargs)
        print(f'Result: {res} type: {type(res)}')
        return res

    return new_func


@type_logger
def render_input(*args, **kwargs):
    return 1


@type_logger
def calc_cube(x):
    return x ** 3
