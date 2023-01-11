
nums = [1,2,3,4,5,6,7,8,9,10]

# filter even nums using lambda function
# filter(the_function, the_list)
even_list = list(filter(lambda x: x%2==0, nums))
print(even_list)