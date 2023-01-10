def fib(n):
    assert n >= 0 and type(n) is int, "Invalid entry."

    if n in {0,1}:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print([fib(n) for n in range(15)])