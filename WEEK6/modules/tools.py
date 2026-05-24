def add(a, b):
    return a + b

def main():
    print(add(1,2))

if __name__ == "__main__":
    main()

from datetime import datetime as dt
print(dt.now())

def make_counter():
    n = 0
    def rtrn():
        nonlocal n
        n += 1
        print(n)
    return rtrn

c = make_counter()
c()
c()
c()

x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
    print(x)
outer()
print(x)

# list = [1, 2, 3]
# print(list(range(5)))
#list is used as an inter so function won't work

x
import math as m
def public_names(library):
    library_dir = dir(library)
    attributes = []
    for attribute in library_dir:
        if not attribute.startswith('_'):
            attributes.append(attribute)
    return attributes
print(public_names(m))


def add_item(item, bag=None):
    bag = []
    bag.append(item)
    return bag
print(add_item(3))
print(add_item(3))
print(add_item(3))




from geometry.circle import area as carea
from geometry.rectangle import area as rarea

print(carea(5))
print(rarea(4, 6))

