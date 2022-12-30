

# words = ["hi", "hello", "hey", "kumusta", "como estas", "privet"]
words = ["kumusta", "como estas", "salam"]

start_tuple = ('h', 'p')

for word in words:
    if word.startswith(start_tuple):
        print(f"starts with {start_tuple}: {word}")
        break
    else:
        print(f"Does not start with any letter from the tuple: {word}")
else:   # this will be triggered if no break statement was satisfied within the preceding for loop
    print(f"No element starts with {start_tuple}")

