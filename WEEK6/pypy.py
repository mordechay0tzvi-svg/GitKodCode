def min_max(tpl):
    i = 0
    max ,min = tpl[i], tpl[i]
    while not isinstance(tpl[], int):
        max ,min = tpl[i], tpl[i]
        i += 1
        if i > len(tpl):
            return "there's no numbers in this tuple"
    for i in tpl:
        try:
            if i > max:
                max = i
            elif i < min:
                min = i
        except:
            pass
    return (max, min)
print(min_max(('s','e','e')))
