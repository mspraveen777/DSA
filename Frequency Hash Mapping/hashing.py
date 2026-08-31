# Brute Force
n = [1, 2, 3, 8, 9, 7, 4, 10, 6, 2, 5, 3]
m = [1, 5, 10, 3, 12]


# for num in m:
#     count = 0
#     for x in n:
#         if x == num:
#             count += 1
#     print(f"{num}:{count}")

# Optimal Solution

# hash_lst = [0] * 11
# for num in n:
#     hash_lst[num] += 1
# for x in m:
#     if x < 0 or x > 10:
#         print(f"{x}: 0")
#     else:
#         print(f"{x}: {hash_lst[x]}")

# Using Dictionary

# hash_dict = {}
# for num in n:
#     if num in hash_dict:
#         hash_dict[num] += 1
#     else:
#         hash_dict[num] = 1
# for num in m:
#     if num in hash_dict:
#         print(f"{num}: {hash_dict[num]}")
#     else:
#         print(f"{num}: 0")


hash_list = [0] * 11
for num in n:
    hash_list[num] += 1
for i in m:
    if i < 0 or i > 10:
        print(f"{i}: 0")
    else:
        print(f"{i}: {hash_list[i]}")
