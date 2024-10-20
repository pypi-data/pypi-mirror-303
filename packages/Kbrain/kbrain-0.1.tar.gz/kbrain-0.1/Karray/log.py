def log(a, b):
    num = 0
    pm = 1
    for _ in range(100000):
        if a ** num > float(b):
            if a ** (num + 1) != float(b):
                num -= (pm * 0.1)
            else:
                num -= pm
        elif a ** num < float(b):
            if a ** (num + 1) != float(b):
                num += (pm * 0.1)
            else:
                num += pm
        elif a ** num == float(b):
            return num

    return num

def root(x, y):
    return x ** (1/y)

def power(x, y):
    return x ** y

print(power(10, log(10, 27)))