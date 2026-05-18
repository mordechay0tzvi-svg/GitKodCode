#1
def filter(lst):
    return list(set(lst))
# print(filter([1, 2, 2, 3, 1, 4, 3]))

#2
def count_unique(lst):
    st = set(lst)
    length_of_unique = 0
    for item in st:
        length_of_unique += 1
    return length_of_unique
# print(count_unique([1,1,1,1,1,1,2,3,4,5]))

#3
def common(lst1, lst2):
    return list(set(lst1) & set(lst2))
# print(common([1, 2, 3, 4], [3, 4, 5, 6]))

#4
def only_one(lst1, lst2):
    return set(lst1) ^ set(lst2)
# print(only_one([1, 2, 3, 4], [3, 4, 5, 6]))

#5
def is_subset(a, b):
    return set(a).issubset(set(b))
# print(is_subset( [6,9,8], [2, 3, 4, 5, 6, 7, 8, 9]))

#6
def unique_charachters(word):
    return len(word) == len(set(word))
# print(unique_charachters("hello"))

#7
def first_reapet(lst):
    new_set = set()
    for item in lst:
        len_of_set = len(new_set)
        new_set.add(item)
        if len(new_set) == len_of_set:
            return item
    return None
# print(first_reapet([1, 2, 3, 4]))

#8
def distinct_words(words):
    words_set = set(words.lower().split())
    words = words.lower().split()
    return len(words) - (len(words) - len(words_set))

# print(distinct_words("The cat and the dog and the bird the and the and meow" ))

#9
def pair_sum_exists(numbers,target):
    num_set = set()
    for num in numbers:
        if (target - num) in num_set :
            return True, f"{num} + {target - num}"
        num_set.add(num)
    return False
    
print(pair_sum_exists( [3, 1, 4, 7, 2], 10))

#10
    
    





