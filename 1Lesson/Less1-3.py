from time import time

def DecoratoTime(func):
    def wrapper(arg):
        Start_Time = time()
        Stap = func(arg)
        Finish_Time = time()
        print("Выполнялось в секундах", Finish_Time - Start_Time)
        return Stap
    return wrapper


@DecoratoTime
def GoToNewStep(a):
    b = 0
    for i in range(0, 10000):
        b += a ** i
    return b


n = GoToNewStep(199)
print(n)



