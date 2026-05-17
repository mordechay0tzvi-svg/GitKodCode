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
# sas ={"a": 1}
# print(get_value(sas, 'b'))

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
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Age must be a number")
    if  150 >= age >= 0:
        return age
    else:
        raise ValueError("Age must be between 0 and 150")

# print(set_age(""))

#7
class InsufficientFundsError(Exception):
    pass
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError
    else:
        return balance - amount

#8
def retry(func, n):
    err = None
    try:
        for _ in range(n):
            try:
                func()
            except Exception as e:
                err = e
        raise err
    except ValueError:
        raise ValueError ("n must be number")



#9
def count_errors(funcs):
    num_of_errors = 0
    for func in funcs:
        try:
            func()
        except:
            num_of_errors += 1
    return num_of_errors

#print(count_errors( [lambda: 1, lambda: 1/0, lambda: int("x"), lambda: 2]))

#10
def load_config(path):
    try:
        with open(path, "r") as f:
            first_line = f.readline()
            return int(first_line)
    except Exception as e:
        raise RuntimeError(f"failed to load config from {e}")

load_config('')







