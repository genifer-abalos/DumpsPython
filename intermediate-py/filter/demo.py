

def is_odd(number):
    return number%2 != 0


def square(number):
    return number**2


def div_by_5(number):
    if number % 5 == 0:
        return True
    return False


nums = [1,2,3,4,5,6,7,8,9,10]
odd_list = list(filter(is_odd, nums))
print(odd_list)

square_list = list(filter(square, nums))        # returns the elements in nums[] that satisfy the square function
print(square_list)

times_5_list = list(filter(div_by_5, nums))
print(times_5_list)


