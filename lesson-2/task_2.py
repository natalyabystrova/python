lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'была', '+5', 'градусов']

result = []
for x in lst:
    if x.isdigit():
        result.append(f'"{x.zfill(2)}"')
    elif x[0] in ('+' or '-'):
        result.append(f'"{x[0]}{x[1:].zfill(2)}"')
    else:
        result.append(x)
print(' '.join(result))
