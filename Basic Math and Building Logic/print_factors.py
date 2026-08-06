#  ---BruteForce Apporach---
# def print_factors(n):
#     factors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             factors.append(i)
#     return factors


# print(print_factors(100))


# ----Better Solution----
# def print_factors(n):
#     factors = []
#     for i in range(1, (n // 2) + 1):
#         if n % i == 0:
#             factors.append(i)
#     factors.append(n)
#     return factors
# print(print_factors(10))

from math import sqrt


def print_factors(n):
    factors = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if n // i != i:
                factors.append(n // i)
    factors.sort()
    return factors


print(print_factors(36))
