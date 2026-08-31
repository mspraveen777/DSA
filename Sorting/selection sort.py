nums = [5, 7, 8, 4, 1, 6, 9, 2]


def selection_sort(nums):
    for i in range(0, len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


print(selection_sort(nums))
