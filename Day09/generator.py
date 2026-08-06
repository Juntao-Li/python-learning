def func():
    for i in range(1, 11):
        yield i

def func1():
    for i in range(10, 51, 10):
        yield i

g = func()

print(next(g))

g1 = func1()

for num in g:
    print(num)

for num in g1:
    print(num)

for num in g1:
    print(num)


