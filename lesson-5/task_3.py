tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена']
groups = ['9А', '7В', '9Б', '9В', '8Б''10А',
          '10Б', '9А']


def formatter(arr1, arr2):
    d = len(arr1)
    for i in range(d):
        yield (arr1[i], arr2[i] if len(arr2) > i else None)
        print(type((arr1[i], arr2[i] if len(arr2) > i else None)))

formatter(arr1=tutors, arr2=groups)

for gen in formatter(arr1=tutors, arr2=groups):
    print(gen)

