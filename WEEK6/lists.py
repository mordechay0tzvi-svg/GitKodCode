#1
def sum_list(arr):
    sum = 0
    for  ind in arr:
        sum += ind
    return sum

#2
def find_max(arr):
    max = arr[0]
    for ind in arr:
        if ind > max:
            max = ind
    return max

#3
def count_in(arr,n):
    count = 0
    for ind in arr:
        if ind == n:
            count += 1
    return count

#4
def reverse_list(arr):
    reversed = []
    for ind in arr:
        reversed.insert(0, ind)
    return reversed
# print(reverse_list([1,2,3,4,5,6,7,8,9]))

#5
def filter_list(arr):
    filtered = []
    for ind in arr:
        if ind not in filtered:
            filtered.append(ind)
    return filtered
# print(filter_list([1,1,1,69,2,2,2,3,3,3]))

#6
def distinct_second(arr):
    first = max(arr[0], arr[1])
    second = min(arr[0], arr[1])
    for ind in arr:
        if ind > first:
            second = first
            first = ind
        if second < ind < first:
            second = ind
    if second == first:
            return None
    return second
# print(distinct_second([1,2,3,4,5,5,5,6]))

#7
def merge(arr1, arr2):
    merged = []
    len1 = len(arr1)
    len2 = len(arr2)
    index1 = 0
    index2 = 0
    while True:
        if arr1[index1] < arr2[index2]:
            merged.append(arr1[index1])
            index1 += 1
        elif arr1[index1] >= arr2[index2]:
            merged.append(arr2[index2])
            index2 += 1
        if index1 == len1 or index2 == len2:
            break
    merged.extend(arr1[index1:])
    merged.extend(arr2[index2:])
    return merged

# print(merge([1,2,3,4,5,5,5,6], [1,2,3,4,5,6,7,8,9,11]))


#8
def rotate(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]
    # for _ in range(k):
    #     arr.insert(0, arr.pop())
print(rotate([1,2,3,4,5,6,7,8,9], 2))

