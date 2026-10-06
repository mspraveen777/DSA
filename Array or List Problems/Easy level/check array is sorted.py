nums = [3, 5, 6, 8, 21, 20]


def is_sorted(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


o = is_sorted(nums)
print(o)
