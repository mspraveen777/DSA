def ArmStrong(n):
    num = n
    res = 0
    nod = len(str(n))
    while num > 0:
        ld = num % 10
        res = res + ld**nod
        num = num // 10

    if n == res:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"


print(ArmStrong(123))
