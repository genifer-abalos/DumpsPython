
x = ["a",1,2,3,4]

y = z = x       # not creating a new list, I am pointing to the same object
                # list are mutable objects

print(id(y), id(z), id(x))      # they all have the same id (address)

print(y)
print(z)
print(x)

print("---------------")
z[1] = 7
y[3] = 2
x[2] = 9

# since they all have the same id, when you change one of them, all are changed as well
print(y)
print(z)
print(x)

print("-------------")
# To make a copy (new list object, different id)

x_copy = x[:]
print(x_copy)
x_copy[0] = 'new'
print(x )
print(x_copy)