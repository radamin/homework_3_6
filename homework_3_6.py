# Задача №3
# Sample Input
#  ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам"


input = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_words(list):
    dct = {}
    for word in list:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in dct:
            dct[sorted_word] = []
        dct[sorted_word].append(word)
    ans = []
    for key in dct:
        ans.append(dct[key])
    return ans


print(group_words(input))
