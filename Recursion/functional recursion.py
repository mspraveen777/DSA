# print sum ( 1 to n) using functional recursion


def func(n):
    if n == 1:
        return 1
    return n + func(n - 1)


x = func(10)
print(x)
