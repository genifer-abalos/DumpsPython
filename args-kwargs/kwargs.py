

def print_address(**kwargs):
    print(type(kwargs))     # dictionary
    # the dictionary
    print(kwargs)
    # the values in the dictionary
    for value in kwargs.values():
        print(value)
    # the keys in the dictionary
    for key in kwargs.keys():
        print(key)
    # keys and values
    for key, value in kwargs.items():
        print(f"{key}: {value}")



print_address(street="Zone 7",
              city="Iguig",
              province="Cagayan",
              zip_code=3504)
print("-------------------")
print_address(street="Zone 7",
              house_no="1",
              city="Iguig",
              province="Cagayan",
              zip_code=3504)