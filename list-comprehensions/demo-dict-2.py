nums = [1,2,3,4,5,6,7,8,9,10]
word = 'geniferaba'
# get a (letter, num) pair

# NESTED FOR LOOP in LIST COMPREHENSIONS
pairings = [(letter, num) for letter in word
                for num in nums]
print(pairings)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# this will create tuple for elements -> index based
name_hero_zip_object = zip(names, heroes)
print(list(name_hero_zip_object))

# LIST COMPREHENSION with DICTIONARIES
# let's create a dictionary {'name':'hero'} for each name,hero in zip(names,heroes)
name_hero_dict = {name: hero for name,hero in zip(names,heroes) if name != 'Peter'}
print(name_hero_dict)
