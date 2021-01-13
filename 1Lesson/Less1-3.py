from time import time


def GoToNewStep(a):
    b = 0
    for i in range(0, 10000):
        b += a ** i

    return b



def TimeStartToEnd():
    Start_Time = time()
    Stap = GoToNewStep(199)
    Finish_Time = time()
    print(Finish_Time - Start_Time)





n = GoToNewStep(199)
print(n)



