
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]


# multiple by two all elements in nums[] that are divisible by 3

print(list(filter(lambda x: x%3==0, nums)))

result = list(
    map(lambda res: res*2, filter(lambda x: x%3==0, nums))
)

result2 = list(
    map(lambda res: res*2, list(filter(lambda x: x%3==0, nums)))
)

print(result)
print(result2)