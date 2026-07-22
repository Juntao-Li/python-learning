def max_num(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num

print(max_num(1, 2, 3))
print(max_num(1, 3, 2))
print(max_num(2, 1, 3))
print(max_num(2, 3, 1))
print(max_num(3, 1, 2))
print(max_num(3, 2, 1))
