
def dec_to_bin(n):

    if n == 0:
        return 0

    return n%2 + 10 * dec_to_bin(int(n/2)) 

print(str(dec_to_bin(13)))