
def q8():
    class A:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def print(self):
            print(self.x, self.y)

    class B(A):     # class B inherits A
        def print(self):
            print(self.y, self.x)

    class C(B):     # class C inherits B
        def __init__(self, x, y, z):
            # super(C, self).__init__(x,y)
            super().__init__(x, y)        # inherits x,y from super class A
            self.z = z


    d = A(2,4)
    e = B(4,5)
    g = C(3,4,7)

    # d.print()
    # e.print()

    g.x = g.z

    d.print()
    e.print()
    g.print()


q8()

