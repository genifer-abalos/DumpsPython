
def q9():
    def x(z):
        def q(x, y):
            x = y + z + x
            print(x)
        return q

    for i in range(10):
        func = x(i)     # func will receive q()     *func is of type function
        print(type(func))
        func(i, i-1)      # q(i, i-1)       z = i, x = i, y = i-1; (z, y, x)
                                            # 0 + 0 + -1 = -1 ()   iter 1
                                            # 1 + 1 + 0   = 2 ()   iter 2
                                            # 2 + 2 + 1   = 5 ()   iter 3

q9()