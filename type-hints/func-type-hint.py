import time
from typing import Callable
from typing import AnyStr


def greeting(name: str) -> str:     # the function should return a string is the meaning of -> str
    return "Hello " + name


def calc_time(func: Callable):
    start = time.time()
    func()
    end = time.time()
    print(f"Time: {end - start}s")


print("-------------------------")
print("Calc time")
calc_time(lambda: sorted("Genifer is learning"))


print("-------------------------")
print("Calc time II: passing a callable function as type hint")


def calc_time_2(func: greeting):    # type hint of func should be greeting()
    start = time.time()
    print(func())
    end = time.time()
    print(f"Time: {end - start}s")


calc_time_2(lambda: greeting("genifer"))
calc_time_2(lambda: greeting("gen"))

