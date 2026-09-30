def partition(nums, low, high):
    piviot = nums[low]
    i = low
    j = high
    while i < j:
        while nums[i] <= piviot and i <= high - 1:
            i += 1
        while nums[j] >= piviot and j >= low + 1:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick_sort(nums, low, high):
    if low < high:
        p_indx = partition(nums, low, high)
        quick_sort(nums, low, p_indx - 1)
        quick_sort(nums, p_indx + 1, high)
    return nums


arr = [5, 6, 7, 1, 8, 2]
print(quick_sort(arr, 0, len(arr) - 1))
