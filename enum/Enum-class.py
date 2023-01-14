from enum import Enum


class Colors(Enum):
    WHITE = 0
    BLUE = 1
    RED = 2


FIRST_COLOR = Colors.RED
SECOND_COLOR = Colors.BLUE

print(FIRST_COLOR)          # Colors.RED <- the value of the constants
print(FIRST_COLOR.name)     # RED
print(FIRST_COLOR.value)    # 0

# add new object to the Colors class
Colors.GREEN = 3
print(Colors.GREEN)
FOURTH_COLOR = Colors.GREEN
print(FOURTH_COLOR)

Colors.register(GRAY = 3)
