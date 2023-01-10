nums = [1,2,3,4,5,6,7,8,9,10]

# Generator Expressions
# get n*n for each n in nums but using generators


# def gen_func(nums):
#     for n in nums:
#         yield n*n
# my_gen = gen_func(nums=nums)

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)
