
# we have a div()
# but what if the denominator is 0
# we need to extend the function by creating a decorator
# Decorators are used to change extend the functionality of a function without actually changing the function itself
# let's create a function check() with a function as a parameter

def check(func):
    def zero_denum(a, b):
        if b == 0:
            print("Invalid 0 as denominator")
            return
        func(a, b)

    return zero_denum


@check      # div = check(div)
def div(a, b):
    return a / b


print(div(4,2))
print(div(4,0))
