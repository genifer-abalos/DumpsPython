def q10():
    def d(f):
        print("we are in d()")
        def w(*args, **kwargs):     # wrapper function
            r = f(*args, **kwargs)
            r += 1
            print("we are in w()")
            return r
        return w

    @d          # decorator -> this will call the function d(), and then pass whatever function it is decorating (in this case it is function a())
    def a(x):
        print("we are in a()")
        return x + 1

    print(a(5))

    # Flow breakdown:
    # a(x=5)
    # calls d()
    # d(a(x=5))
    # a returns 6
    # we now have d(6)
    # in w()
    #    6 += 1
    # w wil return 7

q10()

