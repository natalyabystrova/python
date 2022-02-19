import sys


def save_to_file(value):
    with open('./bakery.csv', mode='a', encoding='utf-8') as bakery:
        bakery.write(f'{value}\n')
    print('Writing success')


if __name__ == '__main__':
    args = sys.argv[1:]
    _args_len = len(args)

    if not _args_len or _args_len > 1:
        print('Bad request')
        exit(1)

    _arg_value = None
    try:
        _arg_value = float(args[0])
    except ValueError:
        print('Arg should be a float')
        exit(1)

    save_to_file(_arg_value)
