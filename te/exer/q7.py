

def q7():
    class A:
        def __init__(self, x):
            self.x = x

        def _eq__(self, o):
            print(self.x)
            print(o.x)
            print(self.x == o.x)
            return self.x == o.x

    a = A(2)
    b = A(2)
    # print(a)
    # print(b)


    print(a == b)
    print(a is b)
    print(a is a)
    print(b is a)
    print(a == a)


q7()