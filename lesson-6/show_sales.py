import sys

args = sys.argv[1:]
_args_len = len(args)

if _args_len > 2:
    print('must be 2 args or less')
    exit(1)
_arg_value = None

try:
    if _args_len:
        _arg_value = int(args[0])
except ValueError:
    print('Args should be int')
    exit(1)

with open('./bakery.csv', mode='r', encoding='utf-8') as b:
    results = []
    for i, line in enumerate(b.readlines()):
        if _args_len == 0:
            results.append(float(line))
        elif _args_len == 1:
            if i >= int(args[0]) - 1:
                results.append(float(line))
        elif _args_len == 2:
            if int(args[0]) - 1 <= i <= int(args[1]) - 1:
                results.append(float(line))
    print(results)


