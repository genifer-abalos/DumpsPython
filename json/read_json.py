import json

with open('data.json', 'r') as file:
    json_object = json.loads(file.read())

print(json_object)
print(json_object['people'])
print(json_object['people'][0])
print(json_object['people'][1])

people_list = json_object['people']

for person in people_list:
    print(f"Name: {person['name']}, Age: {person['age']}, Weight: {person['weight']}")
