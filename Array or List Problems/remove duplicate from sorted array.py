nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]

# Brute force method
# def remove_duplicates(nums):
#     freq_map = {}
#     for num in nums:
#         if num not in freq_map:
#             freq_map[num] = 1

#     j = 0
#     for i in freq_map:
#         nums[j] = i
#         j += 1
#     return j, nums

# optimal method


def remove_duplicates(nums):
    i = 0
    j = i + 1
    n = len(nums)
    while j < n:
        if nums[i] != nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    return i + 1, nums


o = remove_duplicates(nums)
print(o)
