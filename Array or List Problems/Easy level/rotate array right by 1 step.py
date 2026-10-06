nums = [3, 6, 7, 8, 9]


# def rotate_array(nums):
#     n = len(nums)
#     nums[:] = [nums[n - 1]] + nums[0 : n - 1]
#     print(nums)


# rotate_array(nums)


def rotate_array(nums):
    n = len(nums)
    temp = nums[n - 1]
    for i in range(n - 2, -1, -1):
        nums[i + 1] = nums[i]
    nums[0] = temp
    return nums


print(rotate_array(nums))
