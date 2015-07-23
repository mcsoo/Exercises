'''Greatest Common Divisor'''
def gcd(m,n):
    while m%n != 0:
        oldm = n
        oldn = m 
        m = oldn
        n = oldm%oldn
    return n
