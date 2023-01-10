nums = [1,2,3,4,5,6,7,8,9,10]

# create a copy array of nums[]
nums_copy = [n for n in nums]
print(nums_copy)

# square all the elements of nums[]
nums_squared = [n**2 for n in nums]
print(nums_squared)

# square all the elements of nums[] if the element is an even number
nums_squared_even = [n**2 for n in nums if n%2==0]
print(nums_squared_even)

# Using a MAP + LAMBDA
# less readable
nums_squared_object = map(lambda n: n**2, nums)  # for all elements of nums[] perform n*2
squared_list = list(nums_squared_object)
print(squared_list)

nums_sqrd_even_object = map(lambda n: n**2 if n%2==0 else None, nums)  # for all elements of nums[] perform n*2 if n is even
squared_even_list = list(nums_sqrd_even_object)
print(squared_even_list)

# Using FILTER + LAMBDA
even_object = filter(lambda n: n%2 == 0, nums)  # for all elements of nums[], filter only those who satisfy n%2==0
even_list = list(even_object)
print(even_list)

