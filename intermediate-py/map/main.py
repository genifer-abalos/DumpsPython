# map function

li = [1,2,3,4,5,6,7,8,9,0]
# FIND the squares of all element if the list li


def func(x):
    return x**x

# way of doing it using loops
# new_list = []
# for i in li:
#     new_list.append(func(i))
# print(new_list)


# using map function
# FOR EVERY ELEMENT IN list li, perform the FUNCTION func
print(map(func, li))        # this will just return the map object
print(list(map(func, li)))  # this will return the list of the map object


# using list comprehension
list_comp = [func(x) for x in li]
list_comp_even = [func(x) for x in li if x%2==0]
print(list_comp)
print(list_comp_even)
