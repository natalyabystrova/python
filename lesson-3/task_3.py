# # Задание 3.
#
# def tresaurus(*words):
#     result = {}
#     for word in words:
#         first_letter = word[0]
#         if first_letter not in result.keys():
#             result[first_letter] = [word]
#         else:
#             result[first_letter].append(word)
#     return result
#
# answer = tresaurus("Иван", "Екатерина", "Ольга", "Илья")
# print(answer, type(answer))