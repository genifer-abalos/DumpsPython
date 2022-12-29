import json


class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def print_person(self):
        print(self.name, self.age, self.weight)

    def get_older(self, years):
        self.age += years

    def save_to_json(self, filename):
        person_detail = {
            'name': self.name,
            'age': self.age,
            'weight': self.weight
        }
        person_json_string = json.dumps(person_detail, indent=4)
        with open(filename, 'w') as file:
            file.write(person_json_string)

    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            person_json_object = json.loads(file.read())

        self.name = person_json_object['name']
        self.age = person_json_object['age']
        self.weight = person_json_object['weight']


p1 = Person('Gen', 26, 56)
p1.print_person()
p1.get_older(1)
p1.save_to_json('Gen.json')


p2 = Person(None, None, None)
p2.load_from_json('Gen.json')
p2.get_older(2)
p2.print_person()