nums = [55, 32, 97, 99, 3, 67]


# largest = max(nums)
# smallest = min(nums)
# print(largest)
# print(smallest)
def largest_element(nums):
    largest = float("-inf")
    for num in nums:
        largest = max(largest, num)
    return largest


o = largest_element(nums)
print(o)
