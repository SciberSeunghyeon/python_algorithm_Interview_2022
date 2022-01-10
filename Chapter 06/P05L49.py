import collections

strs = ["eat","tea","tan","ate","nat","bat"]

str_dic = {}

for word in strs:
    sorted_word = ''.join(sorted(word))
    if not sorted_word in str_dic.keys():
        str_dic[sorted_word] = [word]
    else:
        str_dic[sorted_word] = str_dic[sorted_word] + [word]
    
print([words for words in str_dic.values()])