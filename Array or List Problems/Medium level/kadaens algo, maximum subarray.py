nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# # brute
# def max_subarray(nums):
#     n = len(nums)
#     maxi = float("-inf")
#     for i in range(0, n - 1):
#         sums = 0
#         for j in range(i, n):

#             sums = sums + nums[j]
#             maxi = max(maxi, sums)
#     return maxi


# print(max_subarray(nums))


# optimal

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def max_Subarray(nums):
    n = len(nums)
    maxi = float("-inf")
    tot = 0
    for i in range(0, n):
        tot += nums[i]
        maxi = max(maxi, tot)

        if tot < 0:
            tot = 0
    return maxi


print(max_Subarray(nums))
