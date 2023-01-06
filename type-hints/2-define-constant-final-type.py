from typing import Final

DATABASE: Final = "MySQL"

print(DATABASE)

DATABASE = "MongoDB"        # creates a prompt that DATABASE is 'Final' and could not be reassigned

print(DATABASE)             # will still assign "MongoDB" to DATABASE
