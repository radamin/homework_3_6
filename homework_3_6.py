# Задача №3
# Sample Input
#  ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам"


# input = ["eat", "tea", "tan", "ate", "nat", "bat"]
#
#
# def group_words(list):
#     dct = {}
#     for word in list:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word not in dct:
#             dct[sorted_word] = []
#         dct[sorted_word].append(word)
#     ans = []
#     for key in dct:
#         ans.append(dct[key])
#     return ans
#
#
# print(group_words(input))


# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.


# strings = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
#
#
# def rle(string):
#     zip_data = ''
#     preview = ''
#     count = 1
#     if not string:
#         return ''
#     for char in string:
#         if char != preview:
#             if preview:
#                 zip_data += str(count) + preview
#             count = 1
#             preview = char
#         else:
#             count += 1
#     else:
#         zip_data += str(count) + preview
#         return zip_data
#
#
# print(rle(strings))
