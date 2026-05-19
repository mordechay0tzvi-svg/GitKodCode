from redis.observability import attributes


def add(a, b):
    return a + b

def main():
    print(add(1,2))

if __name__ == "__main__":
    main()

from datetime import datetime as dt
print(dt.now())

import math as m
def public_names(library):
    library_dir = dir(library)
    attributes = []
    for attribute in library_dir:
        if not attribute.startswith('_'):
            attributes.append(attribute)
    return attributes
print(public_names(m))

def add_item(item, bag):
    bag.append(item)
    return bag
print(add_item(3, [1,2]))



from geometry.circle import area as carea
from geometry.rectangle import area as rarea

print(carea(7))
print(rarea(6, 7))