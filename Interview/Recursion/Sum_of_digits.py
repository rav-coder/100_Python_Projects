
def sum(n):
    assert n >= 0 and type(n) is int, "Invalid entry."

    if n==0:
        return 0

    return int(n%10) + sum(int(n/10))

print(sum(14534))

# print(145/10) # returns 14.5 , python does not do integer division by default