nums = [5, 10, -3, -1, -10, 6]


# def rearrrange_element(nums):
#     n = len(nums)
#     result = []
#     postive = []
#     negative = []
#     for i in range(0, n):
#         if nums[i] < 0:
#             negative.append(nums[i])
#         else:
#             postive.append(nums[i])
#     for i in range(0, len(postive)):
#         result.append(postive[i])
#         result.append(negative[i])
#     return result


# print(rearrrange_element(nums))


def rearrange_element(nums):
    n = len(nums)
    result = n * [0]
    pos = 0
    neg = 1
    for i in range(0, n):
        if nums[i] > 0:
            result[pos] = nums[i]
            pos += 2
        else:
            result[neg] = nums[i]
            neg += 2
    return result


print(rearrange_element(nums))
