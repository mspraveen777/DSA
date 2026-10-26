nums = [1, 2, 0, 2, 1, 0, 2, 0, 1, 0]

# Brute
# nums.sort()
# print(nums)


# # Better
# def sort_0s_1s_2s(nums):
#     cnt_0 = 0
#     cnt_1 = 0
#     cnt_2 = 0
#     n = len(nums)
#     for i in range(0, n):
#         if nums[i] == 0:
#             cnt_0 += 1
#         elif nums[i] == 1:
#             cnt_1 += 1
#         else:
#             cnt_2 += 1
#     for i in range(0, cnt_0):
#         nums[i] = 0
#     for i in range(cnt_0, cnt_0 + cnt_1):
#         nums[i] = 1
#     for i in range(cnt_0 + cnt_1, n):
#         nums[i] = 2
#     return nums


# print(sort_0s_1s_2s(nums))

# Optimal


# def sort_nums(nums):
#     n = len(nums)
#     low = 0
#     mid = 0
#     high = n - 1
#     while mid <= high:
#         if nums[mid] == 0:
#             nums[low], nums[mid] = nums[mid], nums[low]
#             mid += 1
#             low += 1
#         elif nums[mid] == 1:
#             mid += 1
#         else:
#             nums[mid], nums[high] = nums[high], nums[mid]
#             high -= 1
#     return nums


# print(sort_nums(nums))


# Mine solution
def sort_nums(nums, left):
    n = len(nums)
    while left < n - 1:
        if nums[left + 1] < nums[left]:
            nums[left], nums[left + 1] = nums[left + 1], nums[left]
        left += 1

    return nums


print(sort_nums(nums, 0))
