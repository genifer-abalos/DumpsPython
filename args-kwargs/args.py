# *args - allows you to pass multiple on-key arguments
# *kwargs - allows you to paa multiple keyword arguments
#       * - unpacking operator
#         1. positional 2. default 3. keyword 4. ARBITRARY

def add(*nums):
    print(type(nums))       # tuple
    total = 0
    for num in nums:
        total += num
    return total


print(add(1, 2, 3, 4))
print(add(1, 2, 3, 4, 5))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")


display_name("Genifer", "Abalos")
display_name("Genifer", "Aurelio", "Abalos")
