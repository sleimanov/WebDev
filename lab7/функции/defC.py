def xor(a, b):
    if a != b:
        return 1
    else:
        return 0

a, b = input().split()
print(xor(int(a), int(b)))