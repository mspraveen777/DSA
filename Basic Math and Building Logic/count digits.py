# n = 5873
# num = n
# count = 0
# while num > 0:
#     num = num // 10
#     count += 1
# print(count)


# or

from math import *


def count(n):
    return int(log10(n) + 1)


print(count(221))
