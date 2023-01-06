from typing import Literal


weekends: Literal['Saturday', 'Sunday']

# weekends = 'Saturday'     # no warning
# weekends = 'Sunday'       # no warning

weekends = 'Monday'         # will generate a warning message
