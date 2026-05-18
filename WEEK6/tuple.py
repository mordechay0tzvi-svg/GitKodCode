#1
def sum_of_tuple(tpl):
    sum = 0
    for i in tpl:
        try:
            sum += i
        except:
            pass
    return sum
#print(sum_of_tuple((1,2,3,"moish",5,6,7,8,9)))

#2
def max_of_tuple(tpl):
    max = tpl[0]
    for i in tpl:
        try:
            if i > max:
                max = i
        except:
            pass
    return max
#print(max_of_tuple((1,2,3,"moish",5,6,7,8,9)))

#3
def count_occurrences(tpl, s):
    count = 0
    for i in tpl:
            if i == s:
                count += 1
    return count
#print(count_occurrences((1,2,2,2,2,2,2,'slslsl',3,4,5,6,7,8,'!9'), 2))

#4
def reverse_tuple(tpl):
    reverse = ()
    for i in range(len(tpl)):
        reverse += (tpl[len(tpl) - i - 1],)
    return reverse
#print(reverse_tuple((1,2,3,4,5,6,7,8,9)))

#5
def swap_pairs(tpl):
    swapped = ()
    for i in range(0, len(tpl) - 1, 2):
        swapped += (tpl[i+1], tpl[i])
    if len(tpl) % 2 == 1:
        swapped += (tpl[len(tpl) - 1],)
    return swapped
#print(swap_pairs((1,2,3,4,5,6,7,8,9)))

#6
def min_max(tpl):
    max ,min = tpl[0], tpl[0]
    for i in tpl:
        try:
            if i > max:
                max = i
            elif i < min:
                min = i
        except:
            pass
    return (max, min)
print(min_max((1,2,'n')))

#7
import math
def distance(point1, point2):
    distance = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return distance
#print(distance((0,0),(3,4)))

#8
def merge_sort(tpl1, tpl2):
    return (sorted(tpl1 + tpl2))


#9
def frequency_table(tpl):
    def filter(tpl):
        filtered = ()
        for i in tpl:
            if i not in filtered:
                filtered += (i,)
        return filtered
    fltr = filter(tpl)
    table = ()
    for item in fltr:
        table += ((item,count_occurrences(tpl, item)))
    return table
print(frequency_table(('a','b','c','b','c','b','a','s','d','c','b','c','a')))

#10
def rotate(tpl,k):
    #return tpl[-k:] + tpl[:-k]
    right = ()
    left = ()
    for i in tpl[-k:]:
        right += (i,)
    for i in tpl[:-k]:
        left += (i,)
    return right + left
#print(rotate((1,2,3,4,5,6,7,8,9), 2))








