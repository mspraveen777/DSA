def func(i, n):
    if i > 4:
        return
    func(i + 1, n)
    print(i)


func(1, 4)
