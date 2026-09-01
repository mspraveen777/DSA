nums = [5, 7, 6, 9, 8, 3, 1, 4]


def bubble_sort(nums):
    for i in range(len(nums) - 2, -1, -1):
        is_swap = False
        for j in range(0, i + 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swap = True

        if is_swap == False:
            return nums

    return nums


# no = [1, 2, 3, 4, 6, 5]
print(bubble_sort(nums))
