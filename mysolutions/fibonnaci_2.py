def fib(num):
    a, b = 0, 1
    print(a)
    while num:
        a, b = b, a + b
        if (a % 2 == 0):
            print(a)
            num -= 1
        else:
            pass

fib(10)
