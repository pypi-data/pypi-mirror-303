import math

def sin(x):
    q = 0
    num = 0
    while q != 85:
        num += ((-1)**q * x**(2*q+1)) / math.factorial(2*q + 1)
        q += 1
    return num

def cos(x):
    q = 0
    num = 0
    while q != 85:
        num += ((-1)**q * x**(2*q)) / math.factorial(2*q)
        q += 1
    return num

def tan(x):
    return sin(x) / cos(x)
