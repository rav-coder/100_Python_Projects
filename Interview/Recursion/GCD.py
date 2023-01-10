
def gcd(x,y):

    if y == 0:
        return x
    else:
        # print(str(y) + ", " + str(x%y))
        return gcd(y, x%y)

print(gcd(8,80))

#######
# gcd(a,0) = 0
# gcd(a,b) = gcd(b, a mod b)