n = 0
num = 0

while True:
    num += ((-1)**n) / (2*n + 1)
    if n == 1000000:
        break
    n += 1

pi = num * 4