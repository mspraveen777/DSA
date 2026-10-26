arr = [1, 3, 1, 2, 7, 3, 3, 3, 3]


# def maximum_element(arr):
#     n = len(arr)
#     res = 0
#     for i in range(0, n):
#         cnt = 1
#         for j in range(i + 1, n):
#             if arr[i] == arr[j]:
#                 cnt += 1
#         if cnt > n // 2:

#             return arr[i]


# print(maximum_element(arr))


# def majority_element(arr):
#     n = len(arr)
#     hash_map = {}
#     cnt = 0
#     for i in range(n):
#         if arr[i] in hash_map:
#             hash_map[arr[i]] += 1
#         else:
#             hash_map[arr[i]] = 1
#     for v in hash_map.values():
#         if v > n // 2:
#             return hash_map[arr[v]]


# print(majority_element(arr))


def majority_element(arr):
    n = len(arr)
    count = 0
    element = None

    for i in range(n):
        if count == 0:
            element = arr[i]
            count = 1
        elif arr[i] == element:
            count += 1
        else:
            count -= 1
    return element


print(majority_element(arr))
