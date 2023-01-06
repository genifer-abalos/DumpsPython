from typing import Union

# We can give one variable more than one type hint

data: Union[int, float] = 3.14
# OR
data_2: int|float = 3.14
data_3: int|float = 3

print(data)
print(data_2)


print(type(data))
print(type(data_2))
print(type(data_3))