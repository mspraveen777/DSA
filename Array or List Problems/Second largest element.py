nums = [55, 32, 97, -55, 45, 32, 87, 21]


# def second_largest(nums):
#     second_large = float("-inf")
#     largest = max(nums)
#     for i in range(0, len(nums)):
#         if second_large < nums[i] < largest:
#             second_large = nums[i]
#     return second_large


# o = second_largest(nums)
# print(o)

sorted(nums)
print(nums[-2])


# optimal solution
def second_largest(nums):
    largest = float("-inf")
    sec_largest = float("-inf")
    for num in nums:
        largest = max(largest, num)
        if num > sec_largest and num != largest:
            sec_largest = num
    return sec_largest


o = second_largest(nums)
print(o)
