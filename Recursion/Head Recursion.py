# Print Your name 4 times
# Using Head Recursion == First Job and then Calls the func

count = 0


def func():
    global count
    if count == 4:
        return

    print("Pravin")
    count += 1
    func()


func()
