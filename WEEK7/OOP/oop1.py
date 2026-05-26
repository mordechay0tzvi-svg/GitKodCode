class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        return (f"{self.name} says woof")
# print(Dog("Rex").bark())

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return(self.width * self.height)
# print(Rectangle(3, 4).area())

class Counter:
    def __init__(self):
        self.val = 0
    def increment(self):
        self.val += 1
    def value(self):
        return self.val

c = Counter()
c.increment()
c.increment()
# print(c.value())

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
# print(Point(1, 2))

class BankAccount:
    def __init__(self,name):
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount

class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
         return (self.celsius * 9/5) + 32
# print(Temperature(100).to_fahrenheit())

class Student:
    school = "ASU"
    def __init__(self,name):
        self.name = name

# print(Student("yochai").school)
# print(Student("levi").school)

class Player:
    players_count = 0
    def __init__(self,name):
        self.name = name
        Player.players_count += 1

# print(Player("john").players_count)
# print(Player("michell").players_count)

class Money:
    def __init__(self, amount):
        self.amount = amount
    def is_more(self, other):
        return self.amount > other.amount
# m1 = Money(100)
# m2 = Money(200)
# print(m1.is_more(m2))

class Playlist:
    def __init__(self):
        self.titles = []
        self.length = 0
    def add(self, title):
        self.titles.append(title)
        self.length += 1
    def remove(self, title):
        try:
            self.titles.remove(title)
            self.length -= 1
        except:
            print("song not found")
    def count(self):
        return self.length
    def __str__(self):
        return [song for song in self.titles]

# playlist1 = Playlist()
# playlist1.add("song1")
# playlist1.add("song2")
# playlist1.remove("song6")
# print(playlist1.count())


