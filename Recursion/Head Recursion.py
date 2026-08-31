# Print Your name 4 times

count = 0


def func():
    global count
    if count == 4:
        return

    print("Pravin")
    count += 1
    func()


func()
