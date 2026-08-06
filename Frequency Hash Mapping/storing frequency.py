nums = [1, 2, 3, 4, 5, 4, 1, 1, 2, 5, 2, 62, 7, 8, 1, 8]

# method 1
# def freq_map(n):
#     seen = {}
#     for num in nums:
#         if num in seen:
#             seen[num] += 1
#         else:
#             seen[num] = 1
#     return seen


# print(freq_map(nums))


# method 2

hash_map = {}
for num in nums:
    hash_map[num] = hash_map.get(num, 0) + 1
print(hash_map)
