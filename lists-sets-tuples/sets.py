#   Set = {} unordered and immutable, but Add/Remove is OK. NO duplicates

fruits = {"apple", "banana", "mango", "grapes", "orange", "lansones"}

print(fruits)   # if you run again, it might return in different order

print(dir(fruits))
# help(fruits)

print("pineapple" in fruits)

fruits.remove("apple")
print(fruits)

fruits.pop()    # random first element since this is a set
print(fruits)

fruits.add("lansones")      # "lansones" is duplicated so this will not create a new lansones element in the set
print(fruits)
