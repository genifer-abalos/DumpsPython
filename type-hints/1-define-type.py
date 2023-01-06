# *Note: Type hints are not mandatory rules
# However, it’s a bad practice and the IDE will remind you
# <variable_name>: <type> = <value>
name: str = "Yang"
age: int = 29
assets: list = []
posts: tuple = ()
hobbies: dict = {}


age = 0.1   # this generates a warning from pycharm ->
            # Expected type 'int', got 'float' instead

# type hint for list with string elements
text_posts: list[str] = ['Simple post 1', 'Simple post 2']
text_posts = [1, 2]     # Expected type 'list[str]', got 'list[int]' instead
text_posts.append(2)

the_dict: dict[str, str] = {'name': 'genifer'}
the_key_dict: dict[int, str] = {1: 'entry 1'}





