
x = [True, 1, "a", "b", "c", 2, "", False, 0, -1]

if any(x):
    print("there's something in there")

for idx, entry in enumerate(x):
    if x[idx]:
        print("not false")
    else:
        print("found a false value")        # "", False, 0