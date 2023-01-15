cube = lambda x: x**3

num_list = range(5)

print([y for x in num_list if (y:= cube(x)) < 30])

print(3**3 + (5+6)**(1+1)  )

# ProcessLookupError
print(dir())

s = {1,1,1,2,2,3,3,3,5}
print(s)