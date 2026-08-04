n = 1234
num = n
res = 0
while num > 0:
    ld = num % 10
    res = res * 10 + ld
    num = num // 10
if n == res:
    print("Palindrome")
else:
    print("Not Palindrome")
