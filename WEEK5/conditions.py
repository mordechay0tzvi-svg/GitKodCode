# 1. Age category

age = int(input("1. Enter age: "))

if age < 0 or age > 120:
    print("Invalid")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teen")
else:
    print("Adult")

# 2. Vowel or consonant


ch = input("\n2. Enter a character: ")

if len(ch) != 1 or not ch.isalpha():
    print("Invalid")
elif ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# 3. Club entry check


age = int(input("\n3. Enter age: "))
vip = input("VIP card? (yes/no): ").lower()

if age < 16:
    print("Rejected")
elif (age > 18 and vip == "yes") or age in [19, 20, 21]:
    print("Allowed")
else:
    print("Rejected")

# 4. Password check

saved_password = "mypassword123"

password = input("\n4. Enter password: ")

if password == saved_password:
    print("Access Granted")
elif len(password) < 8:
    print("Too short")
else:
    print("Wrong password")

# 5. Point inside rectangle

x = int(input("\n5. Enter x: "))
y = int(input("Enter y: "))

if 10 < x < 50 and 20 < y < 80:
    print("Inside the rectangle")
elif (10 <= x <= 50 and (y == 20 or y == 80)) or \
     (20 <= y <= 80 and (x == 10 or x == 50)):
    print("On the edge")
else:
    print("Outside the rectangle")


# 6. Greeting with default

name = input("\n6. Enter your name: ") or "Anonymous"

print("Hello,", name)


# 8. Count positive numbers

a = int(input("\n8. Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

count = (a > 0) + (b > 0) + (c > 0)

print("Positive numbers:", count)

# 10. Grade calculator

score = int(input("\n10. Enter score: "))

grade = "A" if score >= 90 else \
        "B" if score >= 80 else \
        "C" if score >= 70 else "F"

print("Grade:", grade)