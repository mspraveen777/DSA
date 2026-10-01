# nums = [1, 0, 3, 4]
nums = [9, 6, 4, 3, 2, 5, 7, 0, 1]

# Brute
# def missing_num(nums):
#     n = len(nums)
#     for i in range(0, n + 1):
#         if i not in nums:
#             return i

# print(missing_num(nums))


# Better
# def missing_num(nums):
#     n = len(nums)
#     freq = {}
#     for i in range(0, n + 1):
#         freq[i] = 0
#     for num in nums:
#         freq[num] = 1
#     for k, v in freq.items():
#         if v == 0:
#             return k


# print(missing_num(nums))


# Optimal
def missing_num(nums):
    n = len(nums)
    return n * (n + 1) / 2 - sum(nums)


print(missing_num(nums))
