nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]


def max_consecutive_one(nums):
    n = len(nums)
    cunt = 0
    max_cnt = 0
    for i in range(0, n):
        if nums[i] == 1:
            cunt += 1
        else:
            max_cnt = max(max_cnt, cunt)
            cunt = 0
    return max(cunt, max_cnt)


print(max_consecutive_one(nums))
