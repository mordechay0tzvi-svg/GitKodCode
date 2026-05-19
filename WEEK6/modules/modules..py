#1
count = 0
def bump():
    global count
    count += 1
    print(count)
def value():
    return bump()
    
value()
value()
value()

#2



