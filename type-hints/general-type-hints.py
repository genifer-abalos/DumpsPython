from typing import Iterable
from typing import Union, Optional


# Iterable type can be -> lists, tuples, or others
def general_function(nums: Iterable):
    for i in nums:
        print(i)


# We can a None as a possible type
a: Union[int, None] = 123
# OR
a2: Optional[int] = None

# compare the above line to this
a3: int = None

