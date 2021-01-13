def GoToNewStep(a):
    b = 0
    for i in range(0, 10000):
        b += a ** i

    return b

n = GoToNewStep(199)
print(n)
