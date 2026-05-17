# 1
print("1.")

for i in range(1, 11):
    if i == 7:
        break

    if i % 2 == 0:
        continue

    print(i)

print()


# 2
print("2.")

while True:
    password = input("Enter password: ")

    if password == "1234":
        print("Welcome!")
        break
    else:
        print("Try again")

print()


# 3
print("3.")

products = []

while True:
    product = input("Enter product name (done to stop): ")

    if product == "done":
        break

    products.append(product)

print("Products:", products)

print()


# 4
print("4.")

for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            break

        print((row, col))

print()


# 5
print("5.")

text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Vowels:", count)

print()


# 6
print("6.")

for i in range(1, 6):
    for j in range(1, 6):
        print(i, "x", j, "=", i * j)

print()


# 7
print("7.")

text = input("Enter a string: ")

reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print("Reversed:", reversed_text)

print()


# 8
print("8.")

num = int(input("Enter a positive integer: "))

count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        count += 1

    num = num // 10

print("Even digits:", count)

print()


# 9
print("9.")

text = input("Enter a string: ")

new_text = ""

for ch in text:
    new_text += ch * 2

print(new_text)

print()


# 10
print("10.")

highest = 0

while True:
    num = int(input("Enter a positive integer (0 to stop): "))

    if num == 0:
        break

    if num > highest:
        highest = num

print("Highest:", highest)

print()


# 11
print("11.")

text = input("Enter a string: ")

valid = True

for ch in text:
    if not ch.isalnum():
        valid = False
        break

print(valid)

print()


# 12
print("12.")

num = int(input("Enter an integer: "))

reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print("Reversed number:", reversed_num)