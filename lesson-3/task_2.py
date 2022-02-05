# # Задание 2.
# def num_translate_adv(k):
#     kl = k.lower()
#     d1 = {'one': "один", 'two': "два", 'three': "три",
#           'four': "четыре", 'five': "пять", 'six': "шесть",
#           'seven': "семь", 'eight': "восемь", 'nine': "девять", 'ten': "десять"}
#     if k in d1.keys():
#         return d1[k]
#     elif kl in d1.keys() and k.istitle():
#         return d1[kl].capitalize()
#
#
# result_1 = num_translate_adv('Eight')
# result_2 = num_translate_adv('one')
# result_3 = num_translate_adv('random')
#
# print(result_1, type(result_1))
# print(result_2, type(result_2))
# print(result_3, type(result_3))
