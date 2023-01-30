def our_decorator(func):
    print("Start of our_decorator(func) " + func.__name__)
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)

    print("Returning the function_wrapper " + func.__name__)
    return function_wrapper     # the function_wrapper() will only be triggerred here


@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))


foo('foo')