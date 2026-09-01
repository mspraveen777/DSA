# # Reversing the array using recursion

arr = [1, 8, 9, 4, 6, 3, 7, 9]


def ReverseTheArray(array, left, right):
    if left >= right:
        return array
    array[left], array[right] = array[right], array[left]
    return ReverseTheArray(array, left + 1, right - 1)


x = ReverseTheArray(
    arr, 3, 6
)  # it is for some part of the array we can do for the whole array
print(x)

"""Using While loop"""

# array = [1, 2, 3, 4, 5]
# left = 0
# right = len(array) - 1
# while left < right:
#     array[left], array[right] = array[right], array[left]
#     left += 1
#     right -= 1
# print(array)
