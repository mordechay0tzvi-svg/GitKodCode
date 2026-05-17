# 1
def is_even(n):
    return n % 2 == 0


print(is_even(4))
print(is_even(7))

print()


# 2
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(5))

print()


# 3 + 5
def sum_digits(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


def digital_root(n):
    while n >= 10:
        n = sum_digits(n)

    return n


print(digital_root(9875))

print()


# 4
def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("racecar"))
print(is_palindrome("hello"))

print()


# 6
def count_digits(n):
    if n == 0:
        return 1

    count = 0

    while n > 0:
        count += 1
        n //= 10

    return count


print(count_digits(7))
print(count_digits(12345))
print(count_digits(1000))

print()


# 7
def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)

    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return sign * reversed_num


print(reverse_integer(12345))
print(reverse_integer(1200))
print(reverse_integer(7))
print(reverse_integer(-123))

print()


# 8
def move_zeros(nums):
    pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1


nums = [0, 1, 0, 3, 12]
move_zeros(nums)

print(nums)

print()


# 9
numbers = [4, 7, 2, 9, 1, 5]

total = sum(numbers)
average = total / len(numbers)
minimum = min(numbers)
maximum = max(numbers)

print("Sum:", total)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)

print()


# 10
original = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(original) - 1, -1, -1):
    reversed_list.append(original[i])

print(reversed_list)

print()


# 11
def remove_duplicates(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(remove_duplicates(items))