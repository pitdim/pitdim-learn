import asyncio

async def func():
    print("Началось выполнение функции func")
    await asyncio.sleep(.1)
    print("Конец выполнения функции func")
    return 1


async def new_func():
    print("Началось выполнение функции new_func")
    await asyncio.sleep(5)
    print("Конец выполнения функции new_func")
    return 2

async def new_func3():
    print("Началось выполнение функции new_func3")
    await asyncio.sleep(2)
    print("Конец выполнения функции new_func3")
    return 3

async def run_all_funk():
    mass = [func(), new_func(), new_func3()]

    done, panding = await asyncio.wait(mass, timeout=3)
    print("panding - ", panding)
    print("done - ", done)

    for t in panding:
        t.cancel()

    for t in done:
        print(t.result())

asyncio.run(run_all_funk())