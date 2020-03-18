def min(a, b, c, d):
    if a < b and a < c and a < d:
        x = a
    elif b < c and b < d:
        x = b
    elif c < d:
        x = c
    else:
        x = d
    return x

a, b, c, d = input().split()
print(min(int(a), int(b), int(c), int(d)))