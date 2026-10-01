nums = [3, 9, 5, 6, 7, 8, 10, 9]
k = 3


# def rotate_array(nums, k):
#     n = len(nums)
#     rotations = k % n
#     for _ in range(0, rotations):
#         e = nums.pop()
#         nums.insert(0, e)
#     print(nums)


# rotate_array(nums, k)


# Better solution


# def rotate_array(nums, k):
#     n = len(nums)
#     k = k % n
#     nums[:] = nums[n - k :] + nums[: n - k]
#     print(nums)


# rotate_array(nums, k)


# Optimal

k = 3
n = len(nums)


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


reverse(nums, n - k, n - 1)
reverse(nums, 0, n - k - 1)
reverse(nums, 0, n - 1)
print(nums)
