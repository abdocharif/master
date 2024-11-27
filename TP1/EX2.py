def max_tuple(t):
    max = t[0]
    for i in t:
        if i > max:
            max = i
    return max
mon_tuple = (3, 7, 2, 19, 5)
print(max_tuple(mon_tuple))
