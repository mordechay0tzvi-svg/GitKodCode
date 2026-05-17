#1
def safe_int(s):
    try:
        s = int(s)
        return s
    except:
        return None

#2
def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "undefined"

#3
def read_first_line(path):
    try:
        with open(path, 'r') as f:
            file = f.readlines()
            return file[0]
    except FileNotFoundError:
        return None

#4
def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "Missing"

#5
def parse_ints(values):
    ints = []
    for value in values:
        try:
            nt = int(value)
            ints.append(nt)
        except ValueError:
            pass
    return ints

#6
def set_age(age):
    if  150 <= age <= 0:
        return age
    else:
        raise ValueError

#7
class InsufficientFundsError(Exception):
    pass
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError
    else:
        return balance - amount

#8






