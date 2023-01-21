import collections
from collections import namedtuple


Point = namedtuple('Point', 'x y z')
print(Point)    # <class '__main__.Point'>
                # since a namedtuple instance is a class
                # we can create instances of class Point()
p1 = Point(3, 4, 5)     # this will break up 3,4,5 and associate with x,y,z
print(p1)               # Point(x=3, y=4, z=5)

AList = namedtuple('List', ['l1', 'l2', 'l3'])
list_1 = AList([1,2], [1,3], [4,5])     # List(l1=[1, 2], l2=[1, 3], l3=[4, 5])
print(list_1)
print(list_1.l3)                        # [4, 5]


ADict = namedtuple('Dict', {'name', 'age', 'sex'})
print(ADict)

per_1 = ADict('Genifer', 25, 'F')
print(per_1)
print(per_1.name)
print(per_1.age)
# print as dictionary
print(per_1._asdict())
# get fields / keys
print(per_1._fields)
# replace a value with key
per_1 = per_1._replace(name='Genifer Abalos')
print(per_1._asdict())