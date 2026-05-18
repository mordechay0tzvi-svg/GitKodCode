#1
from os import lseek


def sum_values(dict):
    sum = 0
    for value in dict.values():
        try:
            sum += value
        except TypeError:
            pass
    return sum

#2
def max_in_dict(dict):
    max = 0
    max_key = None
    for key, value in dict.items():
        if value > max:
            max = value
            max_key = key
    return max_key
# print(max_in_dict({'a':1,'b':2,'c':3}))

#3
def letters_dict(word):
    letters = {}
    for letter in word:
        if letter not in letters:
            letters[letter] = 1
            continue
        else:
            letters[letter] += 1
    return letters
# print(letters_dict('banana'))

#4
def inver_dict(dict):
    inverted = {}
    for key, value in dict.items():
        inverted[value] = key
    return inverted

# print(inver_dict({"a": 1, "b": 2, "c": 3}))


#5
def merge_dicts(dict1, dict2):
    merged = {}
    for key, value in dict1.items():
        merged[key] = value
    for key, value in dict2.items():
        merged[key] = value
    return merged
# print(merge_dicts({"a": 1, "b": 2}, {"b": 20, "c": 30} ))

#6
def filter_by_value(dict, value):
    filtered = {}
    for k, v in dict.items():
        if v >= value:
            filtered[k] = v
    return filtered
#print(filter_by_value({"a": 1, "b": 5, "c": 3, "d": 8},7))

#7
def group_by_letter(lst):
    dict = {}
    for word in lst:
        if word[0] in dict:
            dict[word[0]].append(word)
        else:
            dict[word[0]] = [word]
    return dict
# print(group_by_letter( ["apple", "ant", "banana", "berry", "cherry"]))

#8
def word_frequancy(words):
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict
# print(word_frequancy(['am','am','why','me']))

#9
def common_keys(dict1, dict2):
    common = []
    for k in dict1.keys():
        for key in dict2.keys():
            if k == key:
                common.append(k)
    return common
#print(common_keys({"a": 1, "b": 2, "c": 3}, {"b": 9, "c": 8, "d": 7} ))

#10
def most_frequant_value(dict):
    frequancy_dict = {}
    for k, v in dict.items():
        if v in frequancy_dict:
            frequancy_dict[v] += 1
        else:
            frequancy_dict[v] = 1
    max_v = 0
    for v in frequancy_dict.values():
        if v > max_v:
            max_v = frequancy_dict[v]
    return max_v
# print(most_frequant_value({"a": 1, "b": 2, "c": 1, "d": 3, "e": 1} ))

