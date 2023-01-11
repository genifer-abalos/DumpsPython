# Containers - stores multiple objects
# lists, tuples, dict, tuple (immutable)

# Types
# 1 - Counter, 2 - Deque, 3 - namedTuple(), 4 - orderedDict, 5 - defaultdict

# Counter

from collections import Counter

c = Counter('gallad')
c2 = Counter([1,2,3,4,1])
c3 = Counter(['a','A','b','b','c'])
c4 = Counter({'name': 'gen', 'nick': 'dim'})
d = Counter(cats=9, dogs=7)

# will produce a key-value pair
print(c)
print(c2)
print(c3)
print(c4)

# to get the value
instances_of_b = c3['b']
print(instances_of_b)

num_of_dogs = d['dogs']
print(num_of_dogs)

# we have an initial list of counts and vaccinated counts
ini = Counter(students=150, teachers=9, admin=3)
vaccinated = Counter(students=100, teachers=7, admin=3)

# Union -> ini + vaccinated
# Intersection -> ini - vaccinated
# Present in both (minimum) -> ini & vaccinated
# Present at most (maximum) -> ini | vaccinated
count_of_not_vaccinated = ini - vaccinated
print(count_of_not_vaccinated)
print(ini+vaccinated)
print(ini-vaccinated)
print(ini & vaccinated)
print(ini | vaccinated)

print("-----------")
# we can also pass a list then subtract that list from the initial Counter instance
tickets = Counter(red=50, blue=40, green=60)
distributed_ticket_lists = ['red','red','blue','green','green','blue','red']
tickets.subtract(distributed_ticket_lists)      # remove the distributed tickets from the tickets initial counter instance
print(tickets)
tickets.update(distributed_ticket_lists)        # undo
print(tickets)
tickets.clear()                                 # remove all
print(tickets)


