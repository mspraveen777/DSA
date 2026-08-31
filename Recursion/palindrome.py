# s = "Gadag"
# left = 0
# right = len(s) - 1


# def Palindrome(s, left, right):
#     s = s.lower()
#     if left > right:
#         return "Palindrome"
#     if s[left] != s[right]:
#         return "Not Palindrome"
#     return Palindrome(s, left + 1, right - 1)


# s = Palindrome(s, left, right)
# print(s)


"""Using WHile Loop"""

s = "n21iti12n"
left = 0
right = len(s) - 1
while left < right:
    if s[left] != s[right]:
        print("Not Palindrome")
        break
    left += 1
    right -= 1
else:
    print("Palindrome")
