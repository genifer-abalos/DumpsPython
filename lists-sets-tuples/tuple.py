
fruits = ("apple", "banana", "mango", "grapes", "orange", "lansones")

print(dir(fruits))
# help(fruits)

print(len(fruits))

print(fruits.index("mango"))

print(fruits.count("grapes"))

fruit_add = ("test",)

fruits = fruits.__add__(fruit_add)

print(fruits)
