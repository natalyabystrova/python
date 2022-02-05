## Задание 5.

# import random
#
# nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
# adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
# adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
#
#
# def get_jokes(n, a, b, c):
#     """ Функция выбирает рандомное число из списка"""
#     result = []
#     for i in range(n):
#         string = f'{random.choice(a)} {random.choice(b)} {random.choice(c)}'
#         result.append(string)
#     print(result)
#
#
# get_jokes(3, nouns, adverbs, adjectives)
# get_jokes(5, a=nouns, b=adverbs, c=adjectives)