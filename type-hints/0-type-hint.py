
# Function with no type hint
# def clean_data(data):
#     print(type(data))
#     print(data)


# function with type hint
def capitalize_data_string(data: str):
    print(type(data))
    print(data)
    print(data.upper())


data = "Genifer"
# data = 1
# data = True
# data = {'key': 'value'}
capitalize_data_string(data)

