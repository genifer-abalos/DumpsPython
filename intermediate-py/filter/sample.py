
# in nums[]
# get the squares of elements in nums[] that are divisible by 7

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

def div_by_7(number):
    return number%7==0

def square(number):
    return number**2

# let's filter the nums/7==0 first
# then square them

div_7_list = list(filter(div_by_7, nums))
print(div_7_list)

square_of_div_7_list = list(map(square, div_7_list))
print(square_of_div_7_list)