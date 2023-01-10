nums = [1,2,3,4,5,6,7,8,9,10]
numss = [1,1,1,1,2,2,3,4,4,5,6,7,7,7,7,7,8,9,9,9,10,1,7,3]

my_set = set()
for n in numss:
    my_set.add(n)
print(my_set)

# SET COMPREHENSION
the_set = {num for num in nums}
print(the_set)