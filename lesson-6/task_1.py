result = []
with open('./nginx_logs.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        end_idx = line.find('- -')
        first_elem =line[:end_idx]
        second_elem = line[(line.find('] "')+3):line.find(' /downloads')]
        third_elem = line[line.find('/downloads'): line.find(' HTTP/')]
        result_tuples = (first_elem, second_elem, third_elem)
        result.append(result_tuples)
    print(result)


