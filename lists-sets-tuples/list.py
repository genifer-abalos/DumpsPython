# collection= single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove is OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
#   Dictionaries = {}


fruits = ["apple", "banana", "mango", "grapes", "orange", "lansones"]

# fruits[<START_INDEX>::<MOVEMENT(- if in reverse)_OR_STEP>]
print(fruits[0:3])
print(fruits[0:3])
print(fruits[::2])
print(fruits[0::2])
print(fruits[1::2]) # from index 1, get element every 2 step
print(fruits[::-1]) # whole list in reverse
print(fruits[1::-1]) # from index 1 , then in reverse
print(fruits[-1::-1]) # from last index , then in reverse
print(fruits[::-2]) # from last index, get element every 2 step
print(fruits[-2::-2]) # from second index from last, get element every 2 step
print(fruits[-3::-2]) # from third index from last, get element every 2 step

print(dir(fruits))
# help(fruits)

print("apple" in fruits)

# fruits.remove("apple")
fruits.insert(0, "test")
fruits.sort()
fruits.reverse()

print(fruits.index("test"))

print(fruits)

