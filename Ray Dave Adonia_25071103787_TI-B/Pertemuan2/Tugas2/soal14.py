def rk(a, b):
    if b == 0:
        return 1
    else:
        return a * rk(a, b - 1)

a = 2
b = 5
hasil = rk(a, b)
