# Brute Force

s = "azyyxyyaaxxuu"
q = ["d", "a", "y", "u"]

# BruteForce Apporach
# for ch in q:
#     count = 0
#     for c in s:
#         if c == ch:
#             count += 1
#     print(f"{ch}: {count}")


# optimal solutions

hash_lst = [0] * 26
for ch in s:
    index = ord(ch) - 97
    hash_lst[index] += 1
for ch in q:
    index = ord(ch) - 97
    print(f"{ch}:{hash_lst[index]}")
