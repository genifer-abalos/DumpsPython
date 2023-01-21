import collections
from collections import deque # pronounced as DECK


d = deque("Hello")
print(d)
d.append('4')
print(d)
d.appendleft(5)
print(d)
d.pop()
print(d)
print(d.popleft())
print(d)

# remove everython
d.clear()
print(d)

d.extend('456')
print(d)
d.extend('extend')
print(d)
d.extendleft('hey')
print(d)            # will add in reverse to the left: hey -> yeh

d.rotate(-1)        # will rotate at the last element
print(d)
d.rotate(-2)
print(d)
d.clear()

print("--------------------")
new_d = deque("hello", maxlen=5)    # can nly accomodate 5
print(new_d)                        # deque(['h', 'e', 'l', 'l', 'o'], maxlen=5)
new_d.extend([1,2,3])
print(new_d)                        # deque(['l', 'o', 1, 2, 3], maxlen=5)