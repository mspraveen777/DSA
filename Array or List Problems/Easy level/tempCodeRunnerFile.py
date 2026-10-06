rray(nums, k):
    n = len(nums)
    k = n % k
    nums[:] = nums[n - k :] + nums[: n - k]
    print(nums)


rotate_array(nums, k)