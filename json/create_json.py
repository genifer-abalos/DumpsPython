import json

the_dict = {
    'people':[
        {
            'name': 'Genifer',
            'age': 25,
            'weight': 56,
        },
        {
            'name': 'Dima',
            'age': 26,
            'weight': 60,
        },
        {
            'name': 'Fer',
            'age': 39,
            'weight': 65,
        },
    ]
}

# CREATE a JSON from a Dictionary
# json_string = json.dumps(the_dict)
json_string = json.dumps(the_dict, indent=4)
print(json_string)

# write the dictionary to a json file
with open('data.json', 'w') as file:
    file.write(json_string)

