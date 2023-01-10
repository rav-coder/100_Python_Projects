
def power(base, exp):

    assert type(exp) is int, "This program can only take integer exponents"

    if base == 0:
        return 0

    if exp==0:
        return 1

    if exp < 0:
        exp = -exp
        return 1 / (base * power(base,exp-1))
    else:
        return base * power(base,exp-1)

print(power(2,-2))