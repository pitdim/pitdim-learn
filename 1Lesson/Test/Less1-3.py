from time import time
import functools


def decorator_time(func):
    @functools.wraps(func)
    def wrapper(*arg):
        start_time = time()
        return_func = func(*arg)
        finish_time = time()
        print("Выполнялось в секундах", finish_time - start_time)
        return return_func
    return wrapper


@decorator_time
def go_to_new_step(a):
    b = 0
    for i in range(0, 10000):
        b += a ** i
    return b


def hello(q, w):
    print("Привет", q, w)


#n = go_to_new_step(199)
#print(n)

print(go_to_new_step.__name__)

hello("Вася", "Питерский")
