nums = [5, 3, 6, 9, 4, 8]
target = 13


# Brute Force
# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(0, n - 1):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# o = two_sum(nums, target)
# print(o)


# Optimal Solution


def two_sum(nums, target):
    hash_map = {}
    n = len(nums)
    for i in range(0, n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [i, hash_map[remaining]]
        hash_map[nums[i]] = i


print(two_sum(nums, target))
