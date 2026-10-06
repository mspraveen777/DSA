nums = [5, 3, 8, 9, 55, 9, 6, 10, 63, 7]
target = 4


def linear_search(nums, target):
    n = len(nums)
    for i in range(0, n):
        if nums[i] == target:
            return i
    return -1


print(linear_search(nums, target))
